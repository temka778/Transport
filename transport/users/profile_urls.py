from django.urls import path

from .views import Profile

app_name = 'profile'

urlpatterns = [
    path('', Profile.as_view(), name='profile')
]