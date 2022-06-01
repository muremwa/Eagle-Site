from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # /blog/
    path('', views.AllPostsPage.as_view(), name='home'),

    # /blog/posts/post-1/
    path('posts/<slug:slug>/', views.PostPage.as_view(), name='post'),

    # /blog/api/posts/
    path('api/posts/', views.AllPostsApi.as_view(), name='api-home'),
]
