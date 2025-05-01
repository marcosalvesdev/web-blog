from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from blog.forms import PostForm
from blog.models import Post


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    form_class = PostForm

    def get_url_success(self):
        return self.get_object().get_absolute_url()


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy("blog:admin_area")


class AdminAreaView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/admin_area.html"
    context_object_name = "posts"
    ordering = ["-created"]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return super().get_queryset()

        return super().get_queryset().filter(author=self.request.user)
