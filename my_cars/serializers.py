
from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    def create(self, validated_data):
        car = Car.objects.create(**validated_data)
        car.save()
        return car

class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('model', 'year', 'image')
