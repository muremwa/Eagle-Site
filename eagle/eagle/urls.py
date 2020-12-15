from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from wing import views as wing_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # home page
    path('', wing_views.HomePage.as_view(), name='home'),

    # about/
    path('about/', wing_views.ResumePage.as_view(), name='resume'),

    # services
    path('services/', wing_views.ServicesPage.as_view(), name='services'),

    # portfolio/
    path('portfolio/', wing_views.PortfolioPage.as_view(), name='portfolio'),

    # contact/
    path('contact/', wing_views.ContactPage.as_view(), name='contact'),

    # extension stats data
    path('tools/extension/<str:extension_id>/', wing_views.extension_data, name='extension_stats'),

    # blog/
    path('blog/', include('blog.urls')),

    # serve media files
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # serve static files
    re_path('^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),


]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
