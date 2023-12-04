from django.urls import path
from auth_app.views import UserView

app_name = 'auth_app'

urlpatterns = [
    path('', UserView.as_view(), name="user"),
]
