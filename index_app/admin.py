from django.contrib import admin
from index_app.models import (
    Const
)


@admin.register(Const)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["kind_price"]
