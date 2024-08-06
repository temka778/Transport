from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model() 


class Technique(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'
    
    def __str__(self):
        return self.name