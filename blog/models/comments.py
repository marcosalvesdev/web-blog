from django.contrib.auth.models import User
from django.db import models


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="_comments")
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="_comments",
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"
