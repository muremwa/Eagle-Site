from datetime import date
from re import compile as re_compile, search as re_search

from django.views import generic
from django.shortcuts import get_object_or_404, redirect, reverse
from django.http import Http404
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostsFilter:
    date_match = re_compile(r'^\d{4}-\d{2}-\d{2}$')
    year_match = re_compile(r'^\d{4}')
    request = None

    def mutate_single_year(self, year_string, begin):
        date_string = year_string

        if re_search(self.year_match, year_string):
            suffix = '01-01' if begin else '12-31'
            date_string = f'{year_string}-{suffix}'

        return date_string

    def get_queryset(self):
        q_set = Post.objects.filter(published__exact=True).order_by('-created')

        # filter by author's name
        if 'author' in self.request.GET:
            q_set = q_set.filter(author__name__icontains=self.request.GET.get('author', ''))

        # filter by tags
        if 'tag' in self.request.GET:
            q_set = q_set.filter(tags__name__icontains=self.request.GET.get('tag', ''))

        try:
            # posts before said date
            if 'before' in self.request.GET:
                _date_ = self.mutate_single_year(self.request.GET.get('before', ''), True)

                if re_search(self.date_match, _date_):
                    date_ = [int(i) for i in _date_.split("-")]
                    date_ = date(date_[0], date_[1], date_[2])
                    q_set = q_set.filter(created__lt=date_)

            # posts on the said date
            if 'on' in self.request.GET:
                _date_ = self.request.GET.get('on', '')

                if re_search(self.date_match, _date_):
                    date_ = [int(i) for i in _date_.split("-")]
                    date_min = date(date_[0], date_[1], date_[2])
                    date_max = date(date_[0], date_[1], date_[2] + 1)
                    q_set = q_set.filter(created__gte=date_min)
                    q_set = q_set.filter(created__lt=date_max)

            # posts after said date
            if 'after' in self.request.GET:
                _date_ = self.mutate_single_year(self.request.GET.get('after', ''), False)

                if re_search(self.date_match, _date_):
                    date_ = [int(i) for i in _date_.split("-")]
                    date_ = date(date_[0], date_[1], date_[2])
                    q_set = q_set.filter(created__gt=date_)

        except ValueError:
            pass

        return q_set


# blog home
class AllPostsPage(PostsFilter, generic.ListView):
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    model = Post

    def get(self, request, *args, **kwargs):
        if bool(request.GET.get('open')):
            return super().get(request, *args, **kwargs)

        search_options = request.GET.urlencode()
        search_suffix = f'?{search_options}' if search_options else ''
        return redirect(f"{reverse('blog:home')}open/{search_suffix}")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(dict(self.request.GET.items()))
        return context


# individual post
class PostPage(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_single.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if not context['post'].published:
            raise Http404

        return context

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


# all posts api
class AllPostsApi(PostsFilter, ListAPIView):
    serializer_class = PostSerializer


# individual post api
class PostApi(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


# create a new comment
class CommentCreateApi(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class BlogApplication(generic.TemplateView):
    template_name = 'blog/open_blog.html'
