from django.db import models
from my_cars.models import Car
from django.conf import settings

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Покупатель')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая стоимость')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    is_confirmed = models.BooleanField(default=False, verbose_name='Подтвержден')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'