from django import forms

from blog.models import Like


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ["author", "post", "value"]
