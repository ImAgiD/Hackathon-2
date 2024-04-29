from rest_framework.serializers import ModelSerializer

from .models import Comment, Rating

class CommentSerilalizer(ModelSerializer):
    class Meta:
        model = Comment
        # fields = 'post', 'body', 'created_at', 'updated_at'
        exclude = ['user']
        
    def validate(self, attrs):
        super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user
        return attrs
    
class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'