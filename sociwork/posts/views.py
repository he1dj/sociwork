from rest_framework.viewsets import ModelViewset
from .models import Post
from .serializers import PostSerializer

class PostViewsets(ModelViewset):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
        
        