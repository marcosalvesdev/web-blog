from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("blog:index")


class UserLogoutView(LogoutView):
    template_name = "accounts/logout.html"
    next_page = reverse_lazy("accounts:logout")
