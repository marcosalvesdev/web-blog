from django import forms

from accounts.models import Profile


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            "bio",
            "location",
            "image",
            "website",
            "occupation",
            "interests",
        )
        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write your bio here...",
                    "rows": 4,
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your location",
                }
            ),
            "website": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your website URL",
                }
            ),
            "occupation": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your occupation",
                }
            ),
            "interests": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your interests",
                }
            ),
        }
