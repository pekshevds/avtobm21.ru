from dataclasses import dataclass
from decimal import Decimal
from django.db.models import QuerySet
from django.db.models import Model
from catalog_app.models import Good
from price_app.models import Price
from wish_list_app.models import WishList
from price_app.services import current_kind


def fetch_users_wish_list(user: Model) -> QuerySet:
    """Возвращает выборку элементов избранного пользователя user"""
    @dataclass
    class Data:
        good: Good
        price: Decimal

    items = list()
    queryset = WishList.objects.filter(user=user)
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
            price=price
        )
        items.append(item)
    return items


def add_to_wish_list(user: Model, good: Model) -> None:
    """Добавляет в избранное пользователя user элемент good"""
    queryset = WishList.objects.filter(user=user, good=good)
    if not queryset:
        WishList.objects.create(user=user, good=good)


def delete_from_wish_list(user: Model, good: Model) -> None:
    """Удаляет из избранного пользователя user элемент good"""
    queryset = WishList.objects.filter(user=user, good=good)
    queryset.delete()


def clear_wish_list(user: Model) -> None:
    """Очищает избранное пользователя user"""
    queryset = WishList.objects.filter(user=user)
    queryset.delete()
