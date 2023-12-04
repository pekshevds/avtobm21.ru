from django.db import models
from auth_app.models import User
from catalog_app.models import Good


class WishList(models.Model):
    good = models.ForeignKey(
        Good,
        on_delete=models.PROTECT,
        verbose_name="Номенклатура",
        related_name="wish_list_items"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Пользователь",
        related_name="wish_list_items"
    )

    def __str__(self) -> str:
        return self.good.name

    class Meta:
        verbose_name = "Строка избранного"
        verbose_name_plural = "Избранное"
