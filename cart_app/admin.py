from django.contrib import admin
from cart_app.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('good', 'user', 'quantity', 'id',)
