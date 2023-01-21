from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile

# Create your views here.


class SignupView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + "?register"

    def get_form(self, form_class=None):
        form = super(SignupView, self).get_form()
        form.fields["username"].widget = forms.TextInput(
            attrs={"class": "form-control mb-2", "placeholder": "Username"})
        form.fields["email"].widget = forms.EmailInput(
            attrs={"class": "form-control mb-2", "placeholder": "Email"})
        form.fields["password1"].widget = forms.PasswordInput(
            attrs={"class": "form-control mb-2", "placeholder": "Password"})
        form.fields["password2"].widget = forms.PasswordInput(
            attrs={"class": "form-control mb-2", "placeholder": "Repeat password"})
        return form


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(
            user=self.request.user)
        return profile
