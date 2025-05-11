from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about-us/", views.AboutView.as_view(), name="about"),
    path("post/create/", views.CreatePostView.as_view(), name="create_post"),
    path("post/<str:slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/<str:slug>/update/", views.UpdatePostView.as_view(), name="update_post"),
    path("post/<str:slug>/delete/", views.DeletePostView.as_view(), name="delete_post"),
    path(
        "post/comment/create/<str:slug>/",
        views.CommentCreateView.as_view(),
        name="create_comment",
    ),
    path("post/like/<str:slug>/", views.LikeView.as_view(), name="like"),
    path("admin_area/", views.AdminAreaView.as_view(), name="admin_area"),
]
