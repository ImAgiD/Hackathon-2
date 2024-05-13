from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Car(models.Model):
    manufacturer = models.ForeignKey(User, on_delete=models.CASCADE, max_length=100, verbose_name='Производитель', blank=True,null=True)
    model = models.CharField(max_length=100, verbose_name='Модель')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='img/', blank=True, verbose_name='Фото')
    year = models.DateTimeField(auto_now_add=True, verbose_name='Год')

    def str(self):
        return f"{self.model} ({self.year})"