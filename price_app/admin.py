from django.contrib import admin
from price_app.models import (
    KindPrice,
    Price
)


@admin.register(KindPrice)
class KindPriceAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ["__str__", "price"]
