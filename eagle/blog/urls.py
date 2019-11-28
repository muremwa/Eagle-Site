from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.AllPostsPage.as_view(), name='home'),

    path('posts/<slug:slug>/', views.PostPage.as_view(), name='post'),
]
