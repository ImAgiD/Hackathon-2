
# from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class Post(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор', blank=True)
    
#     title = models.CharField(max_length=100, verbose_name='Название')
    
#     image = models.ImageField(upload_to='posts_img/', blank=True, verbose_name='Фото')
    
#     description = models.TextField(blank=True, verbose_name='Описание')
    
#     created_at = models.DateTimeField(auto_now_add=True)
    
        
#     def __str__(self):
#         return self.title
    
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Car(models.Model):
    manufacturer = models.ForeignKey(User, on_delete=models.CASCADE, max_length=100, verbose_name='Производитель', blank=True)
    model = models.CharField(max_length=100, verbose_name='Модель')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='img/', blank=True, verbose_name='Фото')
    year = models.DateTimeField(auto_now_add=True, verbose_name='Год')

    def __str__(self):
        return f"{self.model} ({self.year})"
    