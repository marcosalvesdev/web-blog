from django import forms
from blog.models import Post
from crispy_forms.helper import FormHelper


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "excerpt", "image"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your post title"}
            ),
            "excerpt": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write your post excerpt here...",
                    "rows": 4,
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write your post content here...",
                    "rows": 12,
                }
            ),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }
