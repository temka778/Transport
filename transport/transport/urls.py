from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('services.urls', namespace='services')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls'))
]
