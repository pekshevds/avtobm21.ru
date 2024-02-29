from django.utils.html import format_html
from django.contrib import admin
from image_app.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'preview',)
    list_display = ('name', 'id', 'preview',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        result = ''
        if obj.image:
            result = format_html(
                f"'<img src={obj.image.url} style='max-height: 75px;'>"
            )
        return result

    preview.short_description = 'Изображение'
