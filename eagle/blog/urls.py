from django.urls import path, re_path
from . import views

app_name = "blog"

urlpatterns = [
    # /blog/
    path('', views.AllPostsPage.as_view(), name='home'),

    # /blog/posts/post-1/
    path('posts/<slug:slug>/', views.PostPage.as_view(), name='post'),

    # /blog/api/posts/
    path('api/posts/', views.AllPostsApi.as_view(), name='api-home'),

    # /blog/api/posts/post-1/
    path('api/posts/<slug:slug>/', views.PostApi.as_view(), name='api-post'),

    # /blog/api/posts/post-1/new-comment/
    path('api/posts/<slug:slug>/new-comment/', views.CommentCreateApi.as_view(), name='comment-create-api'),

    # blog/open/
    re_path(r'open/(?P<path>.*)', views.BlogApplication.as_view(), name='home-open'),
]
