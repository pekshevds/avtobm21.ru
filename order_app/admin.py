from django.contrib import admin
from order_app.models import Customer
from order_app.models import Organization
from order_app.models import Contract
from order_app.models import Order
from order_app.models import ItemOrder


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn', 'id',)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn', 'id',)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'date',
                    'client', 'customer', 'organization', 'id',)
    search_fields = ('number',)
    list_filter = ('client', 'customer', 'organization',)
    date_hierarchy = 'date'


class ItemOrderInLine(admin.TabularInline):
    model = ItemOrder


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemOrderInLine]
    list_display = ('__str__', 'number', 'date', 'contract',
                    'client', 'customer', 'organization',
                    'author', 'comment', 'id',)
    search_fields = ('number',)
    list_filter = ('client', 'customer', 'organization', 'author',)
    # date_hierarchy = 'date'
