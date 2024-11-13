from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordResetForm
from django.core.exceptions import ValidationError
from .models import User

class CreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'phone_number')


class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'photo']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)


class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not User.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с такой почтой не зарегистрирован.")
        return email