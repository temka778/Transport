from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView

from .forms import CreationForm
from .models import User


app_name = 'users'


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('services:index')
    template_name = 'users/signup.html'


class PasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('auth:password_change_done')

    def get_success_url(self):
        return self.success_url


class Profile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user