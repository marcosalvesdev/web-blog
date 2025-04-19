from django.urls import path
from accounts.views import (
    UserLoginView,
    UserLogoutView,
    UserRegistrationView,
    UserResetPasswordView,
    UserResetDonePasswordView,
    UserPasswordResetConfirmView,
    UserPasswordResetCompleteView,
    UserProfileView,
)

app_name = "accounts"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", UserRegistrationView.as_view(), name="register"),
]

# Profile URLs
urlpatterns += [
    path("profile/<int:pk>/", UserProfileView.as_view(), name="profile"),
]

# Password Reset URLs
urlpatterns += [
    path("password/reset/", UserResetPasswordView.as_view(), name="password_reset"),
    path(
        "password/reset/done/",
        UserResetDonePasswordView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password/reset/<uidb64>/<token>/",
        UserPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password/reset/complete/",
        UserPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
