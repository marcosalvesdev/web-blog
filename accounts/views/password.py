from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeDoneView,
)
from django.urls import reverse_lazy


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
