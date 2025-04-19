from accounts.views.login import UserLoginView
from accounts.views.login import UserLogoutView
from accounts.views.register import UserRegistrationView

from accounts.views.password import UserResetPasswordView
from accounts.views.password import UserResetDonePasswordView
from accounts.views.password import UserPasswordResetConfirmView
from accounts.views.password import UserPasswordResetCompleteView

from accounts.views.profile import UserProfileView
from accounts.views.profile import UpdateProfileView
from accounts.views.profile import UpdateProfileImageView

__all__ = [
    "UserLoginView",
    "UserLogoutView",
    "UserRegistrationView",
    "UserResetPasswordView",
    "UserResetDonePasswordView",
    "UserPasswordResetConfirmView",
    "UserPasswordResetCompleteView",
    "UserProfileView",
    "UpdateProfileView",
    "UpdateProfileImageView",
]
