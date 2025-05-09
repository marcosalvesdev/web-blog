# Generated by Django 5.2 on 2025-04-14 03:40

import django.utils.timezone
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_excerpt"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="created_date",
        ),
        migrations.AddField(
            model_name="post",
            name="created",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="post_images"),
        ),
        migrations.AddField(
            model_name="post",
            name="modified",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
