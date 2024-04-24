# from rest_framework import serializers
# from .models import Post

# class PostSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Post
#         fields = '__all__'

#     def create(self, validated_data):
#         validated_data["author"] = self.context['request'].user
#         post = super().create(validated_data)
#         post.save()
#         return post 
        
# class PostListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('title', 'image', 'author')
        
        
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
