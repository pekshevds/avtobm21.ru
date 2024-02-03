from django.urls import path
from auth_app.views import UserView, SendPinView

app_name = 'auth_app'

urlpatterns = [
    path('', UserView.as_view(), name="user"),
    path('send-pin/', SendPinView.as_view(), name="send-pin-code"),
]
