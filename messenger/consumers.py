import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model

from messenger.models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        current_user_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']
        self.room_name = (
            f'{current_user_id}_{other_user_id}'
            if int(current_user_id) > int(other_user_id)
            else f'{other_user_id}_{current_user_id}'
        )
        self.room_group_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_layer)
        await self.disconnect(close_code)

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        sender_username = data['username']
        receiver_username = data['receiver']

        receiver = await self.get_user(receiver_username)
        sender = await self.get_user(sender_username)

        await self.save_message(sender=sender, receiver=receiver, message=message, thread_name=self.room_group_name)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'senderUsername': sender_username,
            },
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['senderUsername']

        await self.send(
            text_data=json.dumps(
                {
                    'message': message,
                    'senderUsername': username,
                }
            )
        )

    @database_sync_to_async
    def get_user(self, username):
        return get_user_model().objects.filter(username=username).first()

    @database_sync_to_async
    def save_message(self, sender, receiver, message, thread_name):
        Message.objects.create(
            sender=sender, receiver=receiver, message=message, thread_name=thread_name)
