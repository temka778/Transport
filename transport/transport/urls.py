from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from services.sitemaps import TechniqueSitemap


sitemaps = {'techniques': TechniqueSitemap,}


urlpatterns = [
    path('', include('services.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'core.views.page_not_found'
handler403 = 'core.views.permission_denied'
handler500 = "core.views.server_error"