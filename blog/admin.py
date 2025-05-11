from django.contrib import admin

from blog.models import Category
from blog.models import Comment
from blog.models import Like
from blog.models import Post
from blog.models import Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "author", "created", "modified"]
    raw_id_fields = ["author", "category", "tags"]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["published", "created", "modified"]
    search_fields = ["title", "content"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name", "slug"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name", "slug"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "created", "modified"]
    raw_id_fields = ["post", "author"]
    search_fields = ["post__title", "author__username", "content"]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "created", "modified"]
    raw_id_fields = ["post", "author"]
    search_fields = ["post__title", "author__username"]
