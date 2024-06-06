from django.urls import path
from price_app.views import (
    KindPriceView,
    PriceView
)


app_name = 'price_app'

urlpatterns = [
    path('kinds/', KindPriceView.as_view(), name="kinds"),
    path('prices/', PriceView.as_view(), name="prices"),
]
