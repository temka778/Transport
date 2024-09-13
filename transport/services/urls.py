from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('technique/<int:pk>/', views.TechniqueDetail.as_view(template_name='services/technique_detail.html'), name='technique_detail')
]