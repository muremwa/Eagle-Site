from rest_framework.serializers import ModelSerializer, CharField, ImageField, IntegerField

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
    date = CharField(source='get_date')

    class Meta:
        model = Comment
        fields = ('id', 'name', 'message', 'date')


class PostSerializer(ModelSerializer):
    feature_image_url = ImageField(source='feature_image')
    date = CharField(source='get_date')
    author = AuthorSerializer()
    comment_count = IntegerField(source='comment_set.count')
    tags = TagSerializer(source='tags.all', many=True)
    comments = CommentSerializer(source='comment_set', many=True)

    class Meta:
        model = Post
        fields = (
            'id', 'feature_image_url', 'date', 'author', 'comment_count', 'title', 'slug', 'tags', 'comments', 'content'
        )
