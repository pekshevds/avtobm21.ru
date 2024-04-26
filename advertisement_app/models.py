from django.db import models
from django.core.validators import FileExtensionValidator
from pytils.translit import slugify
from server.base import Base
from server.base import Directory
from image_app.models import Image
from catalog_app.commons import secret_from_string


class GroupOfProperty(Directory):
    ordering = models.DecimalField(
        verbose_name="Порядок сортировки",
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        default=0
    )

    class Meta:
        verbose_name = "Группа свойств"
        verbose_name_plural = "Группы свойств объевлений"
        ordering = ["ordering"]


class Property(Directory):
    ordering = models.DecimalField(
        verbose_name="Порядок сортировки",
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        default=0
    )
    group = models.ForeignKey(
        GroupOfProperty,
        on_delete=models.PROTECT,
        verbose_name="Группа свойства",
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        if self.group:
            return f"{self.group.name} / {self.name}"
        return self.name

    class Meta:
        verbose_name = "Свойство"
        verbose_name_plural = "Свойства объявлений"
        ordering = ["ordering"]


class Advertisement(Directory):
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=15,
        decimal_places=2,
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
    specification = models.FileField(
        verbose_name="Спецификация",
        upload_to='docs/',
        blank=True,
        null=True,
        default="",
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    business_offer = models.FileField(
        verbose_name="Коммерческое предложение",
        upload_to='docs/',
        blank=True,
        null=True,
        default="",
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    is_active = models.BooleanField(
        verbose_name="Активен",
        default=False
    )
    description = models.TextField(
        verbose_name="Комментарий",
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(
                f"{self.name}-{secret_from_string(str(self.id))}"
            )
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Рекламное объявление"
        verbose_name_plural = "Объявления"


class AdvertisementsImage(Base):
    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.PROTECT,
        verbose_name="Рекламное объявление",
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
        verbose_name_plural = "Изображения объявления"


class ValuePropertyOfAnAdvertisement(Base):
    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.PROTECT,
        verbose_name="Рекламное объявление",
        related_name="properties"
    )
    property = models.ForeignKey(
        Property,
        on_delete=models.PROTECT,
        verbose_name="Свойство"
    )
    value = models.CharField(
        verbose_name="Значение",
        max_length=1024,
        blank=True,
        null=True,
        default=""
    )

    class Meta:
        verbose_name = "Значение свойства объявления"
        verbose_name_plural = "Значения свойств объявлений"
