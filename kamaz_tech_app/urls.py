from django.urls import path
from kamaz_tech_app.views import LoadServicesView, OrderServicesView


app_name = "kamaz_tech_app"

urlpatterns = [
    path("services-load/", LoadServicesView.as_view(), name="services-load"),
    path("services-orders/", OrderServicesView.as_view(), name="services-orders"),
]
