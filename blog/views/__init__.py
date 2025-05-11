from blog.views.about import AboutView
from blog.views.comment import CommentCreateView
from blog.views.index import IndexView
from blog.views.like import LikeView
from blog.views.post import AdminAreaView
from blog.views.post import CreatePostView
from blog.views.post import DeletePostView
from blog.views.post import PostDetailView
from blog.views.post import UpdatePostView

__all__ = [
    "IndexView",
    "PostDetailView",
    "CreatePostView",
    "AboutView",
    "AdminAreaView",
    "UpdatePostView",
    "DeletePostView",
    "CommentCreateView",
    "LikeView",
]
