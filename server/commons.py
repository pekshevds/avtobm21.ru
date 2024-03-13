from django.db import transaction
from catalog_app.services.category import (
    default_category
)
from catalog_app.services.good import (
    goods_with_empty_category
)


def fill_empty_categories() -> None:
    with transaction.atomic():
        category = default_category()
        goods = goods_with_empty_category()
        for good in goods:
            good.category = category
            good.save()
