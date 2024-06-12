from django.db import models
from server.base import Directory
from catalog_app.models import Good


class KindPrice(Directory):

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Вид цены"
        verbose_name_plural = "Виды цен"


class Price(models.Model):
    kind = models.ForeignKey(
        KindPrice,
        verbose_name="Вид цены",
        on_delete=models.CASCADE,
        related_name="prices"
    )
    good = models.ForeignKey(
        Good,
        verbose_name="Товар",
        on_delete=models.CASCADE,
        related_name="prices"
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=15,
        decimal_places=2,
        default=0
    )

    def __str__(self) -> str:
        return f"{self.kind} - {self.good}"

    class Meta:
        verbose_name = "Запись регистрации цен"
        verbose_name_plural = "Цены"
        unique_together = [["kind", "good"]]
