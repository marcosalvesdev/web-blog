from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        verbose_name="Profile Picture",
        upload_to="accounts/profiles/images",
        null=True,
        blank=True,
    )
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(max_length=200, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    interests = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.user.username}"
