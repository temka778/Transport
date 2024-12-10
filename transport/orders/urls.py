from django.urls import path
from .views import CreateOrderView, delete_order

app_name = 'orders'

urlpatterns = [
    path('delete-order/<int:order_id>/', delete_order, name='delete_order'),
    path('create_order/<int:technique_id>/', CreateOrderView.as_view(), name='create_order'),
]