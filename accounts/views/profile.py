from django.views.generic import DetailView, UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import ProfileUpdateForm, UserUpdateForm


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/profile.html"
    slug_field = "username"

    def get_queryset(self):
        return super().get_queryset().select_related("profile")


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "accounts/profile_update.html"
    slug_field = "username"

    def get_queryset(self):
        return super().get_queryset().select_related("profile")

    def get_success_url(self):
        return reverse_lazy(
            "accounts:profile", kwargs={"slug": self.request.user.username}
        )

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if "profile_form" not in context_data:
            context_data["profile_form"] = ProfileUpdateForm(
                instance=self.request.user.profile
            )
        return context_data

    def post(self, request, *args, **kwargs):
        data = request.POST
        user_form = self.form_class(data=data, instance=request.user)
        profile_form = ProfileUpdateForm(
            data=data, files=request.FILES, instance=request.user.profile
        )

        user_form_is_valid = user_form.is_valid()
        profile_form_is_valid = profile_form.is_valid()

        if user_form_is_valid and profile_form_is_valid:
            profile_form.save()
            return self.form_valid(user_form)

        return self.render_to_response(
            context=self.get_context_data(form=user_form, profile_form=profile_form)
        )


class UpdateProfileImageView(UpdateProfileView):
    template_name = "accounts/profile.html"
    form_class = ProfileUpdateForm
    slug_field = "username"

    def post(self, request, *args, **kwargs):
        files = request.FILES
        if files:
            profile_form = self.form_class(files=files, instance=request.user.profile)

            if profile_form.is_valid():
                profile_form.save()

        return redirect(self.get_success_url())
