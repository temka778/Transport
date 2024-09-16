from django.urls import path
from .views import CreateOrderView, ajax_order_form

app_name = 'orders'

urlpatterns = [
    path('create/<int:technique_id>/', CreateOrderView.as_view(), name='create'),
    path('ajax_order_form/<int:technique_id>/', ajax_order_form, name='ajax_order_form'),
]
