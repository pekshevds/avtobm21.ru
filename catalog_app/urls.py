from django.urls import path
from catalog_app.views import (
    ManufacturerView,
    FilteringView,
    PasteurizationView,
    GassingView,
    TradeMarkView,
    CategoryView,
    GoodView
)


app_name = 'catalog_app'

urlpatterns = [
    path('manufacturer/', ManufacturerView.as_view(), name="manufacturer"),
    path('filtering/', FilteringView.as_view(), name="filtering"),
    path('pasteurization/', PasteurizationView.as_view(), name="pasteurization"),
    path('gassing/', GassingView.as_view(), name="gassing"),
    path('trade-mark/', TradeMarkView.as_view(), name="trade-mark"),
    path('category/', CategoryView.as_view(), name="category"),
    path('good/', GoodView.as_view(), name="good"),
]
