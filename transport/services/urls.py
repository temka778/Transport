from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('technique/<int:pk>/', views.TechniqueDetail.as_view(), name='technique_detail')
]