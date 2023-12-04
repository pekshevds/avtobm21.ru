from django.db import models
from server.base import Directory


class Image(Directory):
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="images/",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
