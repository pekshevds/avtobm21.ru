from collections import namedtuple
from django.db import models
from server.base import Base
from price_app.models import KindPrice


class Const(Base):
    kind_price = models.ForeignKey(
        KindPrice,
        verbose_name="Вид цен",
        on_delete=models.PROTECT
    )

    def save(self, *args, **kwargs):
        """
        Синглтон - обеспечивает наличие не более одной записи"""
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    @classmethod
    def info(cls):
        Const = namedtuple("Const", [
            "kind_price",
        ])

        item = cls.objects.first()
        if item:
            return Const(
                kind_price=item.kind_price
            )
        return Const(
            kind_price=None)

    class Meta:
        verbose_name = "Константы"
        verbose_name_plural = "Константы"
        ordering = ["-created_at"]
