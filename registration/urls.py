from django.urls import path
from .views import SignupView, ProfileUpdate

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
]
