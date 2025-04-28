from django.contrib.auth.models import User
from django.db import models


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="_likes")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
