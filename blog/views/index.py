from django.views.generic import ListView
from blog.models import Post


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-created"]

    def get_queryset(self):
        return super().get_queryset().select_related("author")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_post"] = self.get_queryset().order_by("-created").first()
        context["posts"] = context["posts"].exclude(id=context["featured_post"].id)[:6]
        return context
