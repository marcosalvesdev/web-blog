from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        prepopulated_fields = {"slug": ("title",)}
        model = Post
        fields = ["image", "title", "slug", "excerpt", "content", "category", "tags"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your post title"}),
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
                },
            ),
        }

    def clean_slug(self):
        slug = self.cleaned_data["slug"]

        if self.changed_data and "slug" not in self.changed_data:
            return slug

        if Post.objects.filter(slug=slug).exists():
            raise forms.ValidationError("This slug is already in use.")
        return slug
