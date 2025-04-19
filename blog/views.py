from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post
from blog.forms import PostForm


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


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/create_post.html"
    form_class = PostForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about_view(request):
    return render(request, "blog/about.html")
