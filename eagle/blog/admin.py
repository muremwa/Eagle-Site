from django.contrib import admin
from .models import Author, Post, Tag, Comment, Entry

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Entry)
admin.site.register(Comment)
