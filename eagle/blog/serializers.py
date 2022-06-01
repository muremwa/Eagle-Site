from rest_framework.serializers import ModelSerializer, IntegerField, CharField, ImageField

from .models import Post, Comment, Tag, Author


class AuthorSerializer(ModelSerializer):
    id = IntegerField(source='pk')
    bio = CharField(source='about')
    image = ImageField(source='avatar')

    class Meta:
        model = Author
        fields = ('name', 'image', 'bio', 'id')
