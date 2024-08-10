from django.db import models


class Technique(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'
    
    def __str__(self):
        return self.name