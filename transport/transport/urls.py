from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('services.urls', namespace='services')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.auth_urls', namespace='auth')),
    path('user/', include('users.profile_urls', namespace='profile')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)