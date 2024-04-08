from django.utils.html import format_html
from django.contrib import admin
from advertisement_app.models import (
    GroupOfProperty,
    Property,
    AdvertisementsImage,
    Advertisement,
    ValuePropertyOfAnAdvertisement
)


@admin.register(GroupOfProperty)
class GroupOfPropertyAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'ordering',)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'group', 'ordering',)


class AdvertisementsImageInLine(admin.TabularInline):
    model = AdvertisementsImage
    fields = ('image', 'preview',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            str = f"<img src={obj.image.image.url} style='max-height: 75px;'>"
            return format_html(str)


class ValuePropertyOfAnAdvertisementInLine(admin.TabularInline):
    model = ValuePropertyOfAnAdvertisement
    fields = ('property', 'value',)


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    inlines = [AdvertisementsImageInLine,
               ValuePropertyOfAnAdvertisementInLine]
    list_display = (
        'name', 'is_active', 'price', 'preview',
    )
    search_fields = ('name',)

    def preview(self, obj):
        if obj.image:
            str = f"<img src={obj.image.image.url} style='max-height: 75px;'>"
            return format_html(str)

    preview.short_description = 'Изображение (превью)'
