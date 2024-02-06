from django.urls import path
from auth_app.views import (
    UserView,
    PinView,
    TokenView
)

app_name = 'auth_app'

urlpatterns = [
    path('', UserView.as_view(), name="user"),
    path('get-pin/', PinView.as_view(), name="get-pin"),
    path('get-token/', TokenView.as_view(), name="get-token"),
]
