from typing import Any

from rest_framework.serializers import ModelSerializer, CharField, ImageField, IntegerField, EmailField, URLField
from django.shortcuts import get_object_or_404

from .models import Post, Comment, Tag, Author


class AuthorSerializer(ModelSerializer):
    bio = CharField(source='about')
    image = ImageField(source='avatar')

    class Meta:
        model = Author
        fields = ('name', 'image', 'bio', 'id')


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name', 'slug')


class CommentSerializer(ModelSerializer):
    date = CharField(source='get_date', read_only=True)
    email = EmailField(write_only=True)
    stamp = IntegerField(source='created_timestamp')

    class Meta:
        model = Comment
        fields = ('id', 'name', 'message', 'date', 'email', 'stamp')

    def validate(self, attrs: Any) -> Any:
        slug = self.context.get('view').kwargs.get('slug')

        if slug:
            post = get_object_or_404(Post, slug=slug)
            attrs.update({'post_id': post.pk})

        return super().validate(attrs)


class PostSerializer(ModelSerializer):
    feature_image_url = ImageField(source='feature_image')
    date = CharField(source='get_date')
    author = AuthorSerializer()
    comment_count = IntegerField(source='comment_set.count')
    tags = TagSerializer(source='tags.all', many=True)
    comments = CommentSerializer(source='comment_set', many=True)
    stamp = IntegerField(source='created_timestamp')
    comment_url = URLField(source='get_comment_url')

    class Meta:
        model = Post
        fields = (
            'id', 'feature_image_url', 'date', 'author', 'comment_count',
            'title', 'slug', 'tags', 'comments', 'content', 'stamp', 'comment_url'
        )
