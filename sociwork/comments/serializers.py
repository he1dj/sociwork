from rest_framework.serializers import ModelSerializer

# Local files
from .models import Comments


class CommentSerializer(ModelSerializer):
    
    class Meta:
        model = Comments
        fields = '__all__'
        

class CommentCreateSerializer(ModelSerializer):
    
    class Meta:
        model = Comments
        fields = ['post','text', 'parent']