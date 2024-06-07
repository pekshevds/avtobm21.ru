from decimal import Decimal
from index_app.models import Const
from django.contrib.auth.models import AnonymousUser


def current_price(good: object, user: object) -> Decimal:
    if user is None or isinstance(user, AnonymousUser):
        info = Const.info()
        kind_price = info.kind_price
        record = good.prices.filter(kind=kind_price).first()
        if record:
            return record.price
    kind_price = user.kind_price
    record = good.prices.filter(kind=kind_price).first()
    if record:
        return record.price
    return Decimal("0")
