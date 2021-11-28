from django.contrib import admin
from .models import Portfolio, EagleProfile, UserMessage, EagleExperience, EagleEducation


@admin.register(EagleProfile)
class EagleProfileModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'bio',  'portrait', 'github', 'linkedin', 'email', 
            ),
        }),
    )


@admin.register(UserMessage)
class UserMessageModelAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Sender Information', {
            'fields': (
                'name', 'email'
            )
        }),
        ('Message', {
            'fields': (
                'date', 'subject', 'message'
            )
        })
    )
    readonly_fields = ('name', 'email', 'date', 'subject', 'message')
    list_display = ('__str__', 'date')


admin.site.register(Portfolio)
admin.site.register(EagleExperience)
admin.site.register(EagleEducation)
