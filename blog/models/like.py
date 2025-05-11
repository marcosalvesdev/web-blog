from django.contrib.auth.models import User
from django.db import models


class Like(models.Model):
    LIKE = 1
    DISLIKE = -1
    LIKE_CHOICES = ((LIKE, "Like"), (DISLIKE, "Dislike"))

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="likes")
    value = models.SmallIntegerField(choices=LIKE_CHOICES, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("author", "post")
