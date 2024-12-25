from django.urls import path
from . import views


app_name = "blog"


urlpatterns = [
    path("", views.PostList.as_view(), name="post-list"),
    path("posts/create/", views.PostCreate.as_view(), name="post-create"),
    path("posts/user/<str:author>/", views.UserPosts.as_view(), name="user-posts"),
    path("posts/<slug:slug>/", views.PostDetail.as_view(), name="post-detail"),
    path("posts/<slug:slug>/update/", views.PostUpdate.as_view(), name="post-update"),
    path("posts/<slug:slug>/delete/", views.PostDelete.as_view(), name="post-delete"),
]
