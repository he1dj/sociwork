from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewsets

router = DefaultRouter()

router.register('post', PostViewsets)

urlpatterns = [
    path('api/', include(router.urls)),
]
