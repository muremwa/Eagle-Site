from django.contrib import admin
from .models import Author, Post, Tag, Comment, Entry


class EntryInline(admin.StackedInline):
    model = Entry
    extra = 3


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published']
    actions = ['publish', 'un_publish', ]
    inlines = [EntryInline, ]
    exclude = ('published',)

    @staticmethod
    def pluralize(set_):
        if set_ == 1:
            return "1 post "
        else:
            return "{set_count} posts ".format(set_count=set_)

    def publish(self, request, queryset):
        updated = queryset.update(published=True)
        self.message_user(request, self.pluralize(updated) + "published.")

    def un_publish(self, request, queryset):
        updated = queryset.update(published=False)
        self.message_user(request, self.pluralize(updated) + "un published.")


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)
