import uuid
from django.db import models
from django.utils import timezone
from django.utils.dateformat import format
from server.base import Directory
from server.base import Document
from catalog_app.models import Good
from client_app.models import Client
from auth_app.models import User
from order_app.services import ganerate_new_number


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
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    contract = models.ForeignKey(
        Contract,
        verbose_name="Договор",
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    client = models.ForeignKey(
        Client,
        verbose_name="Клиент",
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    customer = models.ForeignKey(
        Customer,
        verbose_name="Покупатель",
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    organization = models.ForeignKey(
        Organization,
        verbose_name="Организация",
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )

    def save(self, *args, **kwargs) -> None:
        if not self.number:
            self.number = ganerate_new_number(model=Order)
        if self.contract:
            if not self.client:
                self.client = self.contract.client
            if not self.customer:
                self.customer = self.contract.customer
            if not self.organization:
                self.organization = self.contract.organization
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Заказ №{self.number} от {format(self.date, 'd F Y')}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-number"]


class ItemOrder(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="items"
    )
    good = models.ForeignKey(
        Good,
        on_delete=models.PROTECT,
        null=True,
        blank=True
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
