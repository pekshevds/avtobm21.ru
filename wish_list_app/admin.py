from django.contrib import admin
from wish_list_app.models import WishList


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('good', 'user', 'id',)
