from django.contrib import admin
from .models import Portfolio, EagleDetails, UserMessage, EagleExperience, EagleEducation

admin.site.register(Portfolio)
admin.site.register(EagleDetails)
admin.site.register(UserMessage)
admin.site.register(EagleExperience)
admin.site.register(EagleEducation)
