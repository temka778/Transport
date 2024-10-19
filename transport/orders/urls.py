from django.urls import path
from .views import CreateOrderView, ajax_order_form, delete_order

app_name = 'orders'

urlpatterns = [
    path('create/<int:technique_id>/', CreateOrderView.as_view(), name='create'),
    path('delete-order/<int:order_id>/', delete_order, name='delete_order'),
    path('ajax_order_form/<int:technique_id>/', ajax_order_form, name='ajax_order_form'),
]
