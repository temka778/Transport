from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('group/<int:pk>/', views.twoo_pages),
    path('group/<slug:post_1>/', views.group_posts)
] 