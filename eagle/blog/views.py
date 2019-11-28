from django.views import generic
from django.shortcuts import get_object_or_404, redirect

from .models import Post


# blog home
class AllPostsPage(generic.ListView):
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    model = Post

    def get_queryset(self):
        q_set = Post.objects.all()

        # filter by author's name
        if 'author' in self.request.GET:
            q_set = q_set.filter(author__name__icontains=self.request.GET['author'])

        # filter by tags
        if 'tag' in self.request.GET:
            q_set = q_set.filter(tags__name__icontains=self.request.GET['tag'])

        # posts before said date
        if 'before' in self.request.GET:
            pass

        # posts on the said date
        if 'on' in self.request.GET:
            pass

        # posts after said date
        if 'after' in self.request.GET:
            pass

        return q_set

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        extras = dict(self.request.GET)
        super_lists = [[key, item] for key, item in context.items()] + [[key, item[0]] for key, item in extras.items()]
        return dict(super_lists)


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
