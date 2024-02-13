from django.urls import path
from wish_list_app.views import (
    WishListView,
    WishListAddView,
    WishListDeleteView,
    WishListClearView
)

app_name = 'wish_list_app'

urlpatterns = [
    path('', WishListView.as_view(), name='list'),
    path('add/', WishListAddView.as_view(), name='add'),
    path('delete/', WishListDeleteView.as_view(), name='delete'),
    path('clear/', WishListClearView.as_view(), name='clear'),
]
