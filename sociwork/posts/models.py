import uuid
from django.db import models
from django.conf import settings


class Post(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    descriptiom = models.TextField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    karma = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.author.email
    