from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField('Номер телефона', max_length=15, unique=True)
    email = models.EmailField('Электронная почта', unique=True)
    username = models.CharField(unique=False, max_length=100)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'username']

    def __str__(self):
        return self.phone_number
