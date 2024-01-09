from django.utils.html import format_html
from django.contrib import admin
from image_app.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "preview",)

    def preview(self, obj):
        str = f"<img src={obj.image.url} style='max-height: 75px;'>"
        return format_html(str)
