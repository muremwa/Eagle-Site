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
    



admin.site.register(Portfolio)
admin.site.register(UserMessage)
admin.site.register(EagleExperience)
admin.site.register(EagleEducation)
