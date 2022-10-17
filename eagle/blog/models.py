import datetime
import random

from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


# authors of a post
class Author(models.Model):
    name = models.CharField(max_length=500, help_text="Enter Full name")
    about = models.TextField(help_text="Bio")
    objects = models.Manager()
    avatar = models.ImageField(
        upload_to='blog/authors_avatars/',
        default='blog/default_images/default_author_avatar.png'
    )

    def __str__(self):
        return "Author called {}".format(self.name)


# tag the post
class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True, unique=True)
    objects = models.Manager()

    def __str__(self):
        return "Tag for {}".format(self.name)

    def save(self, *args, **kwargs):
        if self.pk:
            self.slug = slugify(f'{self.name}-{self.pk}')
        else:
            super().save()
            self.slug = slugify(f'{self.name}-{self.pk}')

        return super().save()


# Each blog post
class Post(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    feature_image = models.ImageField(
        upload_to="blog/feature_images",
        default="blog/default_images/default_feature.png"
    )
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(blank=True, null=True, unique=True)
    published = models.BooleanField(default=False, help_text="IF NOT PUBLISHED IT WILL NOT APPEAR ANYWHERE")
    content = models.TextField(help_text='Enter Content Here')
    objects = models.Manager()

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "Blog post titled {}".format(self.title)

    @property
    def created_timestamp(self) -> float:
        stamp = 0

        if self.created:
            stamp = self.created.timestamp()

        if self.pk:
            stamp += self.pk
        else:
            stamp += random.randint(1000, 1000000)

        return stamp

    @property
    def no_feature_image(self):
        return self.feature_image == 'blog/default_images/default_feature.png'

    def get_date(self):
        return self.created.strftime("%B %d, %Y") if self.created else ''

    def get_easy_date(self):
        return self.created.strftime("%Y-%m-%d") if self.created else ''

    def save(self, *args, **kwargs):
        if self.pk:
            self.slug = slugify(f'{self.title}-{self.author.name}-{self.pk}')
        else:
            super().save()
            self.slug = slugify(f'{self.title}-{self.author.name}-{self.pk}')

        return super().save()

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={
            'slug': self.slug,
        })

    def get_comment_url(self):
        return reverse('blog:comment-create-api', kwargs={'slug': self.slug})


# Comments for each post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, help_text="Enter your full name")
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()
    objects = models.Manager()

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "Comment by {owner} on a {post}".format(post=str(self.post).lower(), owner=self.name)

    @property
    def created_timestamp(self) -> float:
        stamp = 0

        if self.created:
            stamp = self.created.timestamp()

        if self.pk:
            stamp += self.pk
        else:
            stamp += random.randint(1000, 1000000)

        return stamp

    def get_date(self):
        clean_date = self.created + datetime.timedelta(0.125)
        return clean_date.strftime("%B %d, %Y at %H:%M%p")

    def get_absolute_url(self):
        return "{post_url}#comment-{comment_pk}".format(
            comment_pk=self.pk,
            post_url=self.post.get_absolute_url()[:-1],
        )
