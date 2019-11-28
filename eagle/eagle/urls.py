from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from wing import views as wing_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', wing_views.HomePage.as_view(), name='home'),

    path('about/', wing_views.ResumePage.as_view(), name='resume'),

    path('services/', wing_views.ServicesPage.as_view(), name='services'),

    path('portfolio/', wing_views.PortfolioPage.as_view(), name='portfolio'),

    path('contact/', wing_views.ContactPage.as_view(), name='contact'),

    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
