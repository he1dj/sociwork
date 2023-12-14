from rest_framework.routers import DefaultRouter
from .views import CommentViewSets
from django.urls import path, include

router = DefaultRouter()
router.register('comments', CommentViewSets)


urlpatterns = [
    path('api/', include(router.urls)),
]