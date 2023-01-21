from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Message

# Create your views here.


@login_required
def threadList(request):
    user = get_user_model().objects.get(username=request.user.username)
    print(user.username)

    threads = Message.objects.filter(sender=user).values(
        'thread_name').distinct() | Message.objects.filter(receiver=user).values(
        'thread_name').distinct()

    threads_user = []
    for thread in threads:
        threads_user += Message.objects.filter(
            thread_name=thread.get('thread_name'))[:1]

    return render(request, 'messenger/my_chats.html', {
        'threads': threads_user,
    })


@ login_required
def chat_page(request, username):
    user_object = get_user_model().objects.get(username=username)
    users = get_user_model().objects.exclude(username=request.user.username)
    thread_name = (
        f'chat_{request.user.id}_{user_object.id}'
        if int(request.user.id) > int(user_object.id)
        else f'chat_{user_object.id}_{request.user.id}'
    )
    messages = Message.objects.filter(
        thread_name=thread_name).select_related('sender')

    user = get_user_model().objects.get(username=request.user.username)

    threads = Message.objects.filter(sender=user).values(
        'thread_name').distinct() | Message.objects.filter(receiver=user).values(
        'thread_name').distinct()

    threads_user = []
    for thread in threads:
        threads_user += Message.objects.filter(
            thread_name=thread.get('thread_name'))[:1]

    context = {
        'users': users,
        'user_object': user_object,
        'messages': messages,
        'threads': threads_user,
    }
    return render(request, 'messenger/chat_personal.html', context)
