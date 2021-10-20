from datetime import datetime

from django.test import TestCase
from django.utils.text import slugify
from django.urls import reverse

from .models import Author, Tag, Comment, Post


class BlogModelsTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name='Muremwa',
            about='Example bio',
        )
        self.tag = Tag.objects.create(
            name='squid'
        )
        self.post = Post.objects.create(
            title='Sample Blog',
            author=self.author,
        )
        self.post.tags.add(self.tag)
        self.comment = Comment.objects.create(
            post=self.post,
            name='Eric',
            email='a@a.com',
            message='sample message given',
        )

    def test_author_model(self):
        author_ = Author.objects.get(pk=1)
        self.assertEqual(author_, self.author)
        self.assertEqual(author_.avatar, 'blog/default_images/default_author_avatar.png')
        self.assertEqual(str(author_), 'Author called Muremwa')

    def test_tag(self):
        tag_ = Tag.objects.get(pk=1)
        self.assertEqual(tag_.name, 'squid')
        self.assertEqual(str(tag_), 'Tag for squid')

    def test_post(self):
        self.post.save()
        self.assertEqual(self.post.created, datetime.date(datetime.today()))
        self.assertEqual(self.post.author, self.author)
        self.assertEqual(self.post.feature_image, 'blog/default_images/default_feature.png')
        self.assertListEqual(
            list(self.post.tags.all()),
            [self.tag]
        )
        self.assertEqual(self.post.slug, slugify(f'{"Sample Blog"}-{self.post.author.name}-{self.post.pk}'))
        self.assertEqual(self.post.published, False)

    def test_comment(self):
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(
            self.comment.get_absolute_url(),
            '{url}#comment-{comment_pk}'.format(
                url=reverse("blog:post", kwargs={"slug": str(self.post.slug)})[:-1],
                comment_pk=self.comment.pk
            )
        )
