from django.contrib import admin
from catalog_app.models import (
    Category,
    Good,
    GoodsImage,
    Model,
    Manufacturer,
    Applicability
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'id',)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'id',)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'id',)


class GoodsImageInLine(admin.TabularInline):
    model = GoodsImage
    fields = ('image',)


class ApplicabilityInLine(admin.TabularInline):
    model = Applicability
    fields = ('model',)


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    inlines = [GoodsImageInLine, ApplicabilityInLine]
    list_display = (
        "name", "art", "category",
        "is_active", "balance", "price",
    )
    search_fields = ("name", "art",)
