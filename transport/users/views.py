from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import CreationForm, ProfileUpdateForm
from .models import User


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('signup_done')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        random_password = get_random_string(length=8)
        user.set_password(random_password)
        user.save()

        send_mail(
            'Ваш аккаунт был создан!',
            f'Ваши данные для входа в личный кабинет https://transport.sytes.net \nЛогин: {user.phone_number}\nПароль: {random_password}',
            None,
            [user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


def signup_done(request):
    template = 'users/signup_done.html'
    return render(request, template)


class Profile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = self.request.user.orders.all()
        return context


class ProfileUpdateView(UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user