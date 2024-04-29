from django.db import models
from django.contrib.auth import get_user_model
from my_cars.models import Car

User = get_user_model()

class Like(models.Model):
    user = models.ForeignKey(User, related_name ='likes', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name ='likes', on_delete=models.CASCADE)
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Car, on_delete=models.CASCADE)
    rating = models.IntegerField()  
    created_at = models.DateTimeField(auto_now_add=True)



