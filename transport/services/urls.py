from django.urls import path
from . import views


app_name = 'services'


urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts')
]