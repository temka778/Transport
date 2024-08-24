from django.db import models
from services.models import Technique
from users.models import User

class Order(models.Model):
    STATUS_CHOICES = [
        ('accepted', 'Заказ принят'),
        ('rejected', 'Заказ отклонён'),
        ('in_progress', 'Заказ в работе'),
        ('completed', 'Заказ завершён'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='Заказчик')
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE, verbose_name='Техника')
    order_date = models.DateTimeField('Дата заказа', auto_now_add=True)
    start_date = models.DateField('Начало аренды')
    end_date = models.DateField('Окончание аренды')
    status = models.CharField('Статус заказа', max_length=20, choices=STATUS_CHOICES, default='accepted')
    total_cost = models.DecimalField('Общая стоимость аренды', max_digits=100, decimal_places=2)
    additional_requirements = models.TextField('Доп. требования', blank=True, null=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Order {self.id} by {self.user.get_full_name()}"

    @property
    def is_active(self):
        return self.status in ['accepted', 'in_progress']