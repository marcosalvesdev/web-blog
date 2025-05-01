from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", blank=True)
    comments = models.ManyToManyField("Comment", blank=True, related_name="_comments")
    likes = models.ManyToManyField("Like", blank=True, related_name="_likes")
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    excerpt = models.TextField(max_length=300)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="posts/images")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/post/{self.slug}/"

    def save(self, **kwargs):
        if not self.published_at and self.published:
            self.published_at = timezone.now()

        return super().save(**kwargs)
