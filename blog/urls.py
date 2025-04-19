from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("create/", views.CreatePostView.as_view(), name="create_post"),
    path("about/", views.AboutView.as_view(), name="about"),
]
