from django.db import models
from django.urls import reverse


class Technique(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    hourly_rate = models.DecimalField('Стоимость аренды за час', max_digits=10, decimal_places=2, null=True, blank=True)
    daily_rate = models.DecimalField('Стоимость аренды за день', max_digits=10, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField('Вес (в тоннах)', max_digits=10, decimal_places=2, null=True, blank=True)
    power = models.DecimalField('Мощность (в л.с.)', max_digits=10, decimal_places=2, null=True, blank=True)
    dimensions = models.CharField('Габариты (ДxШxВ в метрах)', max_length=50, null=True, blank=True)
    fuel_type = models.CharField('Тип топлива', max_length=50, null=True, blank=True)
    capacity = models.IntegerField('Грузоподъемность (в кг)', null=True, blank=True)
    image = models.ImageField('Фото техники', upload_to='technique_images/', null=True, blank=True)

    class Meta:
        verbose_name = "Техника"
        verbose_name_plural = "Техника"

    def get_absolute_url(self):
            return reverse('technique_detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class TechniquePhoto(models.Model):
    technique = models.ForeignKey(Technique, related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='technique_photos/')

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотки"