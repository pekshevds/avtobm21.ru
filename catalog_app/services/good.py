from django.db import transaction
from catalog_app.models import (
    Good
)

from catalog_app.services.category import handle_category
from catalog_app.services.trade_mark import handle_trade_mark
from catalog_app.services.gassing import handle_gassing
from catalog_app.services.pasteurization import handle_pasteurization
from catalog_app.services.filtering import handle_filtering
from catalog_app.services.manufacturer import handle_manufacturer


def good_by_id(good_id: str) -> Good:
    return Good.objects.filter(id=good_id).first()


def handle_good(good_dir: dir) -> Good:
    good_id = good_dir.get('id', "")
    good_name = good_dir.get('name', "")
    good = good_by_id(good_id)
    if good is None:
        good = Good.objects.create(
            id=good_id,
            name=good_name
        )
    return good


def handle_good_list(good_list: None) -> [Good]:
    goods_id = []
    with transaction.atomic():
        for good_item in good_list:
            good = handle_good(good_dir=good_item)
            good.full_name = good_item.get('full_name', good.full_name)
            good.price = good_item.get('price', good.price)
            good.balance = good_item.get('balance', good.balance)
            good.art = good_item.get('art', good.art)
            good.volume = good_item.get('volume', good.volume)
            good.strength = good_item.get('strength', good.strength)
            good.in_package = good_item.get('in_package', good.in_package)
            good.expiration_date = good_item.get('expiration_date',
                                                 good.expiration_date)
            key_name = 'category'
            if key_name in good_item:
                temp_dir = good_item.get(key_name)
                good.category = None if temp_dir is None else \
                    handle_category(temp_dir)

            key_name = 'trade_mark'
            if key_name in good_item:
                temp_dir = good_item.get(key_name)
                good.trade_mark = None if temp_dir is None else \
                    handle_trade_mark(temp_dir)

            key_name = 'gassing'
            if key_name in good_item:
                temp_dir = good_item.get(key_name)
                good.gassing = None if temp_dir is None else \
                    handle_gassing(temp_dir)

            key_name = 'pasteurization'
            if key_name in good_item:
                temp_dir = good_item.get(key_name)
                good.pasteurization = None if temp_dir is None else \
                    handle_pasteurization(temp_dir)

            key_name = 'filtering'
            if key_name in good_item:
                temp_dir = good_item.get(key_name)
                good.filtering = None if temp_dir is None else \
                    handle_filtering(temp_dir)

            key_name = 'manufacturer'
            if key_name in good_item:
                temp_dir = good_item.get(key_name)
                good.manufacturer = None if temp_dir is None else \
                    handle_manufacturer(temp_dir)

            good.save()
            goods_id.append(good.id)

    return Good.objects.filter(id__in=goods_id)
