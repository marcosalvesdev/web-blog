from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin
from django.views.generic.edit import ProcessFormView

from blog.forms import LikeForm
from blog.models import Post


class LikeView(
    LoginRequiredMixin,
    SingleObjectTemplateResponseMixin,
    ModelFormMixin,
    ProcessFormView,
):
    model = Post
    form_class = LikeForm
    template_name = "blog/post_detail.html"

    def get(self, request, *args, **kwargs):
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"slug": self.kwargs["slug"]})

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        data = {
            "author": self.request.user,
            "post": post,
            "value": request.POST.get("value"),
        }
        like = post.likes.filter(author=self.request.user).first()
        form = self.form_class(data=data, instance=like)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
