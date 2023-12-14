from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response

#Local files
from .serializers import CommentSerializer, CommentCreateSerializer
from .models import Comments
from sociwork.posts.models import Post


class CommentViewSets(ModelViewSet):
    queryset = Comments.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    """
    Если получает POST запрос то используется отдельный сериализатор
    """
    def get_serializer_class(self):
        if self.action == 'create':
            return CommentCreateSerializer
        return CommentSerializer
    
    """
    Перед созданием передает id пользователя для comments.user_id
    """
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)