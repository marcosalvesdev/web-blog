from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog.forms import CommentForm
from blog.models import Comment
from blog.models import Post


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/post_detail.html"

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def get(self, request, *args, **kwargs):
        return redirect(reverse_lazy("blog:post_detail", kwargs={"slug": kwargs["slug"]}))

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs["slug"])
        form = self.get_form()
        form.instance.author = self.request.user
        form.instance.post_id = post.id
        if form.is_valid():
            return self.form_valid(form)
        else:
            self.object = None
            self.extra_context = {
                "comment_form": form,
                "post": post,
            }
            return self.form_invalid(form)
