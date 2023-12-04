from django.urls import path
from order_app.views import (
    ContractView,
    OrderView
)

app_name = 'order_app'

urlpatterns = [
    path('', OrderView.as_view(), name="order"),
    path('contract/', ContractView.as_view(), name="contract"),
]
