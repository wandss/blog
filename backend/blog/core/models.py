from django.db import models
from django.contrib.auth import get_user_model

from uuid import uuid4

User = get_user_model()

class Post(models.Model):

    post_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=50)
    tag = models.CharField(max_length=50, null=True, blank=True)
    text = models.TextField()
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.title)
