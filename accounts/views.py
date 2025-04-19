from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeDoneView,
)
from django.views.generic import DetailView, CreateView
from accounts.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("blog:index")


class UserLogoutView(LogoutView):
    template_name = "accounts/logout.html"
    next_page = reverse_lazy("accounts:logout")


class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")


class UserResetPasswordView(PasswordResetView):
    template_name = "accounts/password/reset.html"
    success_url = reverse_lazy("accounts:password_reset_done")
    email_template_name = "accounts/password/reset_email.html"


class UserResetDonePasswordView(PasswordChangeDoneView):
    template_name = "accounts/password/reset_done.html"
    success_url = reverse_lazy("accounts:login")


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "accounts/password/reset_confirm.html"
    success_url = reverse_lazy("accounts:password_reset_complete")


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "accounts/password/reset_complete.html"
    success_url = reverse_lazy("accounts:login")


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/profile.html"
