from django import forms
from django.contrib.auth.forms import UserChangeForm
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