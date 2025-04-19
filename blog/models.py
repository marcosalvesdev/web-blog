from django.db import models
from django.contrib.auth.models import User


# TODO: Add a slug field to be used in urls


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(max_length=300)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="posts/images")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
