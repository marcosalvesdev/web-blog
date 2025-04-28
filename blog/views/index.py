from django.views.generic import ListView

from blog.models import Post


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-created"]

    def get_queryset(self):
        return super().get_queryset().select_related("author")
