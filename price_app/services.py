from typing import Union
from decimal import Decimal
from index_app.models import Const
from django.contrib.auth.models import AnonymousUser


def current_kind(user: object) -> Union[object | None]:
    if user is None or isinstance(user, AnonymousUser):
        info = Const.info()
        return info.kind_price
    if user.client:
        return user.client.kind_price
    return None


def current_price(good: object, user: object) -> Decimal:
    kind_price = current_kind(user=user)
    if kind_price:
        record = good.prices.filter(kind=kind_price).first()
        if record:
            return record.price
    return Decimal("0")
