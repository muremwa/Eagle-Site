from django.views import generic

from .models import Post


# blog home
class AllPostsPage(generic.ListView):
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    model = Post


# individual post
class PostPage(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_single.html'
    slug_url_kwarg = 'slug'
