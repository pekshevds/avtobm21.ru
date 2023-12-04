from django.db import models
from auth_app.models import User
from catalog_app.models import Good


class Cart(models.Model):
    good = models.ForeignKey(
        Good,
        on_delete=models.PROTECT,
        verbose_name="Номенклатура"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Пользователь",
        related_name="cart_items"
    )
    quantity = models.DecimalField(
        verbose_name="Количество",
        max_digits=15,
        decimal_places=3,
        null=True,
        blank=True,
        default=1
    )

    def __str__(self) -> str:
        return self.good.name

    class Meta:
        verbose_name = "Строка корзины"
        verbose_name_plural = "Корзина"
