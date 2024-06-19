from django.utils.html import format_html
from django.contrib import admin
from catalog_app.models import (
    Category,
    Good,
    GoodsImage,
    Model,
    Manufacturer,
    Applicability
)

admin.site.site_header = 'Панель администрирования avtobm21.ru'
admin.site.site_title = 'Панель администрирования avtobm21.ru'
admin.site.index_title = 'Добро пожаловать!'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'ordering',)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id',)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id',)


class GoodsImageInLine(admin.TabularInline):
    model = GoodsImage
    fields = ('image', 'preview',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            str = f"<img src={obj.image.image.url} style='max-height: 75px;'>"
            return format_html(str)


class ApplicabilityInLine(admin.TabularInline):
    model = Applicability
    fields = ('model',)


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    inlines = [GoodsImageInLine, ApplicabilityInLine]
    list_display = (
        'name', 'art', 'clean_art', 'category',
        'is_active', 'balance', 'price', 'preview',
    )
    search_fields = ('name', 'art', 'clean_art',)

    def preview(self, obj):
        if obj.image:
            str = f"<img src={obj.image.image.url} style='max-height: 75px;'>"
            return format_html(str)

    preview.short_description = 'Изображение (превью)'
