from django.db import models
from pytils.translit import slugify
from server.base import Directory
from image_app.models import Image
from catalog_app.commons import secret_from_string


class Category(Directory):

    class Meta:
        verbose_name = "Раздел каталога"
        verbose_name_plural = "Разделы каталога"


class TradeMark(Directory):

    class Meta:
        verbose_name = "Торговая марка"
        verbose_name_plural = "Торговые марки"


class Gassing(Directory):

    class Meta:
        verbose_name = "Газация"
        verbose_name_plural = "Виды газации"


class Pasteurization(Directory):

    class Meta:
        verbose_name = "Пастеризация"
        verbose_name_plural = "Виды пастеризации"


class Filtering(Directory):

    class Meta:
        verbose_name = "Фильрация"
        verbose_name_plural = "Виды фильтрации"


class Manufacturer(Directory):

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Good(Directory):
    full_name = models.CharField(
        verbose_name="Наименование полное",
        max_length=1024,
        blank=True,
        null=True,
        default=""
    )
    art = models.CharField(
        verbose_name="Артикул",
        max_length=25,
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
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=15,
        decimal_places=2,
        blank=True,
        null=True,
        default=0
    )
    volume = models.DecimalField(
        verbose_name="Объем, л",
        max_digits=15,
        decimal_places=3,
        blank=True,
        null=True,
        default=0
    )
    strength = models.DecimalField(
        verbose_name="Крепость, %",
        max_digits=15,
        decimal_places=3,
        blank=True,
        null=True,
        default=0
    )
    in_package = models.DecimalField(
        verbose_name="В упаковке, шт",
        max_digits=15,
        decimal_places=0,
        blank=True,
        null=True,
        default=0
    )
    expiration_date = models.DecimalField(
        verbose_name="Срок годности, мес",
        max_digits=15,
        decimal_places=0,
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
    """code_1c = models.CharField(
        verbose_name="Код из 1С:бухгалтерия 8",
        max_length=11,
        blank=True,
        null=True,
        default="",
        db_column=True
    )"""
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
    trade_mark = models.ForeignKey(
        TradeMark,
        on_delete=models.PROTECT,
        verbose_name="Торговая марка",
        blank=True,
        null=True
    )
    gassing = models.ForeignKey(
        Gassing,
        on_delete=models.PROTECT,
        verbose_name="Газация",
        blank=True,
        null=True
    )
    pasteurization = models.ForeignKey(
        Pasteurization,
        on_delete=models.PROTECT,
        verbose_name="Пастеризация",
        blank=True,
        null=True
    )
    filtering = models.ForeignKey(
        Filtering,
        on_delete=models.PROTECT,
        verbose_name="Фильтрация",
        blank=True,
        null=True
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.PROTECT,
        verbose_name="Производитель",
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(
                f"{self.name}-{secret_from_string(str(self.id))}"
            )
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class GoodsImage(models.Model):
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

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения товара"
