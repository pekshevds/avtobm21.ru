from decimal import Decimal
from django.db import models
from pytils.translit import slugify
from server.base import Base
from server.base import Directory
from image_app.models import Image
from catalog_app.commons import (
    secret_from_string,
    clean_string
)


class Category(Directory):
    ordering = models.IntegerField(
        verbose_name="Параметр сортировки",
        null=True,
        blank=True,
        default=0
    )

    class Meta:
        verbose_name = "Раздел каталога (Код ОКДП2)"
        verbose_name_plural = "Разделы каталога (Классификатор кодов ОКДП2)"
        ordering = ["ordering"]


class Model(Directory):

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"


class Manufacturer(Directory):

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Good(Directory):
    art = models.CharField(
        verbose_name="Артикул",
        max_length=50,
        blank=True,
        null=True,
        default="",
        db_index=True
    )
    clean_art = models.CharField(
        verbose_name="Артикул для поиска",
        max_length=50,
        blank=True,
        null=True,
        default="",
        db_index=True
    )
    balance = models.DecimalField(
        verbose_name="Остаток",
        max_digits=15,
        decimal_places=3,
        blank=True,
        null=True,
        default=0
    )
    slug = models.SlugField(
        max_length=250,
        null=True,
        blank=True,
        unique=True
    )
    image = models.ForeignKey(
        Image,
        on_delete=models.PROTECT,
        verbose_name="Изображение (превью)",
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Раздел каталога",
        related_name="goods",
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        verbose_name="Активен",
        default=False
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.PROTECT,
        verbose_name="Производитель",
        blank=True,
        null=True
    )

    @property
    def price(self) -> Decimal:
        return Decimal("0")

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(
                f"{self.name}-{secret_from_string(str(self.id))}"
            )
        self.clean_art = clean_string(self.art)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class GoodsImage(Base):
    good = models.ForeignKey(
        Good,
        on_delete=models.PROTECT,
        verbose_name="Номенклатура",
        related_name="images"
    )
    image = models.ForeignKey(
        Image,
        on_delete=models.PROTECT,
        verbose_name="Изображение"
    )

    def __str__(self) -> str:
        return self.image.name

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения товара"


class Applicability(Base):
    good = models.ForeignKey(
        Good,
        on_delete=models.PROTECT,
        verbose_name="Номенклатура",
        related_name="applicabilities"
    )
    model = models.ForeignKey(
        Model,
        on_delete=models.PROTECT,
        verbose_name="Модель"
    )

    def __str__(self) -> str:
        return self.model.name

    class Meta:
        verbose_name = "Применяемость"
        verbose_name_plural = "Применяемость"
