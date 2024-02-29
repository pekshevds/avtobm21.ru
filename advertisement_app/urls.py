from django.urls import path
from advertisement_app.views import (
    AdvertisementView
)


app_name = 'advertisement_app'

urlpatterns = [
    path('', AdvertisementView.as_view(), name="advertisement"),
]
