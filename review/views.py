from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import  api_view
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated


from my_cars.models import Car
from .models import Like, Comment
from .serializers import CommentSerilalizer
from .permissions import IsOwnerOrReadOnly


@api_view(['POST'])
def toggle_like(request, id):
    user = request.user
    if not user.is_authenticated:
        return Response(status=401)
    car = get_object_or_404(Car, id=id)
    if Like.objects.filter(user=user, car=car).exists():
        Like.objects.filter(user=user, car=car).delete()        
    else:
        Like.objects.create(user=user, car=car)
    return Response(201)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerilalizer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in self.permission_classes]    