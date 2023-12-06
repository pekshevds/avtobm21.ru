from django.contrib import admin
from auth_app.models import User
from order_app.models import Client


class UserInLine(admin.TabularInline):
    model = User
    fields = ('username',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [UserInLine]
    list_display = ('name', 'id',)
