from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('services.urls', namespace='services')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.auth_urls', namespace='auth')),
    path('user/', include('users.profile_urls', namespace='profile')),
]
