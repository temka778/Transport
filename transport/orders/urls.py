from django.urls import path
from .views import CreateOrderView

app_name = 'orders'

urlpatterns = [
    path('create/<int:technique_id>/', CreateOrderView.as_view(), name='create'),
]
