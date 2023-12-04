from django.db import models
from django.utils import timezone
from django.utils.dateformat import format
from server.base import Directory
from server.base import Document
from catalog_app.models import Good
from order_app.services import ganerate_new_number


class Client(Directory):
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Customer(Directory):
    inn = models.CharField(
        verbose_name="ИНН",
        max_length=12,
        null=True,
        blank=True,
        default="",
        db_index=True
    )

    class Meta:
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагенты"


class Organization(Directory):
    inn = models.CharField(
        verbose_name="ИНН",
        max_length=12,
        null=True,
        blank=True,
        default="",
        db_index=True
    )

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"


class Contract(Directory):
    number = models.CharField(
        verbose_name="Номер",
        max_length=25,
        null=True,
        blank=True
    )
    date = models.DateField(
        verbose_name="Дата",
        null=True,
        blank=True,
        default=timezone.now
    )
    client = models.ForeignKey(
        Client,
        verbose_name="Клиент",
        on_delete=models.PROTECT
    )
    customer = models.ForeignKey(
        Customer,
        verbose_name="Покупатель",
        on_delete=models.PROTECT
    )
    organization = models.ForeignKey(
        Organization,
        verbose_name="Организация",
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return f"№{self.number} от {format(self.date, 'd F Y')}"

    class Meta:
        verbose_name = "Договор"
        verbose_name_plural = "Договоры"


class Order(Document):
    contract = models.ForeignKey(
        Contract,
        verbose_name="Договор",
        on_delete=models.PROTECT
    )
    client = models.ForeignKey(
        Client,
        verbose_name="Клиент",
        on_delete=models.PROTECT
    )
    customer = models.ForeignKey(
        Customer,
        verbose_name="Покупатель",
        on_delete=models.PROTECT
    )
    organization = models.ForeignKey(
        Organization,
        verbose_name="Организация",
        on_delete=models.PROTECT
    )

    def save(self, *args, **kwargs) -> None:
        if not self.number:
            self.number = ganerate_new_number(model=Order)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Заказ №{self.number} от {format(self.date, 'd F Y')}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-number"]


class ItemOrder(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )
    good = models.ForeignKey(
        Good,
        on_delete=models.PROTECT
    )
    quantity = models.DecimalField(
        verbose_name="Количество",
        max_digits=15,
        decimal_places=3,
        null=True,
        blank=True
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True
    )
    summ = models.DecimalField(
        verbose_name="Сумма",
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True
    )
