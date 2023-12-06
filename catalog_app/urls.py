from django.urls import path
from catalog_app.views import (
    ManufacturerView,
    ModelView,
    CategoryView,
    GoodView
)


app_name = 'catalog_app'

urlpatterns = [
    path('manufacturer/', ManufacturerView.as_view(), name="manufacturer"),
    path('model/', ModelView.as_view(), name="model"),
    path('category/', CategoryView.as_view(), name="category"),
    path('good/', GoodView.as_view(), name="good"),
]
