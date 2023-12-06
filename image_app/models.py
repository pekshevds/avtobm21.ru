from django.db import models
from server.base import Base


class Image(Base):
    url = models.CharField(
        max_length=255,
        verbose_name="Путь к изображению"
    )

    def __str__(self) -> str:
        return f"{self.url}"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
