from django.urls import path

from .views import threadList, chat_page


messenger_patterns = ([
    path("", threadList, name="list"),
    path("<str:username>/", chat_page, name="chat"),
], "messenger")
