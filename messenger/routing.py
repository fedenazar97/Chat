from django.urls import path

from messenger import consumers

websocket_urlpatterns = [
    path('ws/messenger/<int:id>/', consumers.ChatConsumer.as_asgi()),
]
