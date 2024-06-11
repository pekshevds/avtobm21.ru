from dataclasses import dataclass
from decimal import Decimal
from django.db.models import QuerySet
from django.db.models import Model
from catalog_app.models import Good
from price_app.models import Price
from cart_app.models import Cart
from price_app.services import current_kind


def fetch_users_cart(user: Model) -> QuerySet:
    """Возвращает выборку элементов корзины пользователя user"""
    @dataclass
    class Data:
        good: Good
        quantity: Decimal
        price: Decimal

    items = list()
    queryset = Cart.objects.filter(user=user)
    prices = Price.objects.filter(
        good__in=[item.good for item in queryset],
        kind=current_kind(user=user)
    )
    for item in queryset:
        price = Decimal("0")
        price_record = prices.filter(good=item.good).first()
        if price_record:
            price = price_record.price
        item = Data(
            good=item.good,
            quantity=item.quantity,
            price=price
        )
        items.append(item)
    return items


def add_to_cart(user: Model, good: Model, quantity: float = 1) -> None:
    """Добавляет в корзину пользователя user элемент good"""
    record = Cart.objects.filter(user=user, good=good).first()
    if not record:
        Cart.objects.create(user=user, good=good, quantity=quantity)
    else:
        record.quantity += quantity
        record.save()


def delete_from_cart(user: Model, good: Model, quantity: float = 1) -> None:
    """Удаляет из корзины пользователя user элемент good"""
    record = Cart.objects.filter(user=user, good=good).first()
    if record:
        if quantity >= record.quantity:
            record.delete()
        else:
            record.quantity -= quantity
            record.save()


def clear_cart(user: Model) -> None:
    """Очищает корзину пользователя user"""
    queryset = Cart.objects.filter(user=user)
    queryset.delete()
