from django.contrib import admin
from image_app.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
