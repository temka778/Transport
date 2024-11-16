from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import CreationForm, ProfileUpdateForm, CustomPasswordResetForm
from .mixins import RedirectAuthenticatedUserMixin
from .models import User


class SignUp(RedirectAuthenticatedUserMixin, CreateView):
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
            f'Ваши данные для входа в личный кабинет https://ННК-Сервис.РФ/ \nЛогин: {user.phone_number}\nПароль: {random_password}',
            None,
            [user.email],
            fail_silently=False,
        )
        self.request.session['allow_signup_done'] = True
        return super().form_valid(form)


def signup_done(request):
    if not request.session.pop('allow_signup_done', False):
        return redirect('index')
    template = 'users/signup_done.html'
    return render(request, template)


class CustomLoginView(RedirectAuthenticatedUserMixin, LoginView):
    template_name="users/login.html"


class Profile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = self.request.user.orders.all().order_by('-order_date')
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name='users/password_reset_form.html'

    def form_valid(self, form):
        self.request.session['allow_password_reset_done'] = True
        return super().form_valid(form)


def password_reset_done(request):
    if not request.session.pop('allow_password_reset_done', False):
        return redirect('index')
    template = 'users/password_reset_done.html'
    return render(request, template)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name='users/password_reset_confirm.html'

    def form_valid(self, form):
        self.request.session['allow_password_reset_done'] = True
        return super().form_valid(form)


def password_reset_complete_view(request):
    if not request.session.pop('allow_password_reset_done', False):
        return redirect('index')
    template='users/password_reset_complete.html'
    return render(request, template)


class CustomPasswordChangeView(PasswordChangeView):
    template_name='users/password_change_form.html'

    def form_valid(self, form):
        self.request.session['allow_password_reset_done'] = True
        return super().form_valid(form)


def password_change_done_view(request):
    if not request.session.pop('allow_password_reset_done', False):
        return redirect('index')
    template='users/password_change_done.html'
    return render(request, template)


class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        return redirect('index')

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')