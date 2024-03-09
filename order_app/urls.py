from django.urls import path
from order_app.views import (
    ContractView,
    OrderView,
    OrderItemView,
    NewOrdersView,
    OrderStatusView,
    PutOrderStatusView
)
from client_app.views import ClientView

app_name = 'order_app'

urlpatterns = [
    path('', OrderView.as_view(), name="order"),
    path('item/', OrderItemView.as_view(), name="order-item"),
    path('contract/', ContractView.as_view(), name="contract"),
    path('client/', ClientView.as_view(), name="client"),
    path('statuses/', OrderStatusView.as_view(), name="statuses"),
    path('put-status/', PutOrderStatusView.as_view(), name="put-status"),
    path('new-orders/', NewOrdersView.as_view(), name="new-orders"),
]
