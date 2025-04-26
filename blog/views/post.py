from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic import DetailView

from blog.forms import PostForm
from blog.models import Post


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/create_post.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
