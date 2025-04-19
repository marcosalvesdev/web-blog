from django.views.generic import CreateView
from accounts.forms import CustomUserCreationForm
from django.urls import reverse_lazy


class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")
