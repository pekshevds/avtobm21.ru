from django.contrib import admin
from auth_app.models import User
from order_app.models import Client
from order_app.models import Customer
from order_app.models import Organization
from order_app.models import Contract
from order_app.models import Order
from order_app.models import ItemOrder


class UserInLine(admin.TabularInline):
    model = User
    fields = ('username',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [UserInLine]
    list_display = ('name', 'id',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn', 'id',)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn', 'id',)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'date',
                    'client', 'customer', 'organization',)
    search_fields = ('number',)
    list_filter = ('client', 'customer', 'organization',)
    date_hierarchy = 'date'


class ItemOrderInLine(admin.TabularInline):
    model = ItemOrder


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemOrderInLine]
    list_display = ('__str__', 'number', 'date', 'contract',
                    'client', 'customer', 'organization', 'comment',)
    search_fields = ('number',)
    list_filter = ('client', 'customer', 'organization',)
    date_hierarchy = 'date'
