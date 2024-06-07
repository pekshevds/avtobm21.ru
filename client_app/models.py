from django.db import models
from server.base import Directory
from price_app.models import KindPrice


class Client(Directory):
    kind_price = models.ForeignKey(
        KindPrice,
        verbose_name="Вид цены",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
