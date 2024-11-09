from django.urls import path
from .views import ajax_order_form, delete_order

app_name = 'orders'

urlpatterns = [
    path('delete-order/<int:order_id>/', delete_order, name='delete_order'),
    path('ajax_order_form/<int:technique_id>/', ajax_order_form, name='ajax_order_form'),
]