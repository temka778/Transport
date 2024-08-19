from django.db import models


class Technique(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость аренды за час", null=True, blank=True)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость аренды за день", null=True, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Вес (в кг)")
    power = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Мощность (в л.с.)")
    dimensions = models.CharField(max_length=255, null=True, blank=True, verbose_name="Габариты (ДxШxВ в метрах)")
    fuel_type = models.CharField(max_length=50, null=True, blank=True, verbose_name="Тип топлива")
    capacity = models.IntegerField(null=True, blank=True, verbose_name="Грузоподъемность (в кг)")
    is_available = models.BooleanField(default=True, verbose_name="Доступна для аренды")
    image = models.ImageField(upload_to='technique_images/', null=True, blank=True, verbose_name="Фото техники")

    class Meta:
        verbose_name = "Техника"
        verbose_name_plural = "Техника"

    def __str__(self):
        return self.name
