from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from blog.forms import CommentForm
from blog.forms import PostForm
from blog.models import Comment
from blog.models import Like
from blog.models import Post


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related("author")
            .prefetch_related(
                Prefetch(
                    lookup="comments",
                    queryset=Comment.objects.order_by("-created").select_related("author__profile"),
                ),
                "likes",
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context["object"]
        user_post_like = post.likes.filter(post__slug=self.kwargs["slug"]).last()
        context["comment_form"] = CommentForm
        if user_post_like:
            context["liked"] = user_post_like.value == Like.LIKE
            context["disliked"] = user_post_like.value == Like.DISLIKE
        return context


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
