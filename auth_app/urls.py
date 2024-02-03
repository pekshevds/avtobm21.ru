from django.urls import path
from auth_app.views import UserView, SendMessageView

app_name = 'auth_app'

urlpatterns = [
    path('', UserView.as_view(), name="user"),
    path('send-message/', SendMessageView.as_view(), name="send-message"),
]
