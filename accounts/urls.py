from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("register/", views.UserRegistrationView.as_view(), name="register"),
]

# Profile URLs
urlpatterns += [
    path("profile/<str:slug>/", views.UserProfileView.as_view(), name="profile"),
    path(
        "profile/<str:slug>/update/",
        views.UpdateProfileView.as_view(),
        name="profile_update",
    ),
    path(
        "profile/<str:slug>/update_image/",
        views.UpdateProfileImageView.as_view(),
        name="profile_update_image",
    ),
]

# Password Reset URLs
urlpatterns += [
    path(
        "password/reset/", views.UserResetPasswordView.as_view(), name="password_reset"
    ),
    path(
        "password/reset/done/",
        views.UserResetDonePasswordView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password/reset/<uidb64>/<token>/",
        views.UserPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password/reset/complete/",
        views.UserPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
