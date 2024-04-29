from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import toggle_like, CommentViewSet, RatingViewSet


router = DefaultRouter()
router.register('comment', CommentViewSet)
router.register('rating', RatingViewSet)

urlpatterns = [
    path('like/<int:id>/', toggle_like),
    path('', include(router.urls)),    
]
