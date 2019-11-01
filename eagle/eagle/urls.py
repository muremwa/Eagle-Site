from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from wing import views as wing_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', wing_views.Home.as_view(), name='home'),

    path('about/', wing_views.Resume.as_view(), name='resume'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
