from django.views import generic
from django.shortcuts import get_object_or_404, redirect, reverse

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

    def post(self, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])
        comment_email = self.request.POST['email']
        if not comment_email:
            comment_email = None

        comment = post.comment_set.create(
            name=self.request.POST['name'],
            email=comment_email,
            message=self.request.POST['message'],
        )

        return redirect(comment.get_absolute_url())
