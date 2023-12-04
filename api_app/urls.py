from django.urls import path, include


app_name = 'api_app'

urlpatterns = [
    path('user/', include('auth_app.urls', namespace='auth_app')),
    path('catalog/', include('catalog_app.urls', namespace='catalog_app')),
    path('wish/', include('wish_list_app.urls', namespace='wish_list_app')),
    path('order/', include('order_app.urls', namespace='order_app')),
]
