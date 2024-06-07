from dataclasses import dataclass
from decimal import Decimal
from typing import List
import json
from threading import Thread
import logging
from django.db.models.query import QuerySet
from django.db.models import Q
from django.db import transaction
from catalog_app.models import (
    Good,
    Model,
    Applicability,
    Category,
    Manufacturer
)
from catalog_app.services.category import (
    handle_category,
    default_category
)
from catalog_app.services.manufacturer import handle_manufacturer
from catalog_app.services.model import handle_model
from django.conf import settings
from price_app.services import current_price


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def goods_with_empty_category() -> QuerySet[Good]:
    return Good.objects.filter(category=None)


def good_by_id(good_id: str) -> Good:
    return Good.objects.filter(id=good_id).first()


def handle_applicability(model: Model, good: Good) -> Applicability:
    applicability = Applicability.objects.filter(
        model=model, good=good
    ).first()
    if not applicability:
        applicability = Applicability.objects.create(
            model=model,
            good=good
        )
    return applicability


def handle_applicability_list(applicability_list: List[dir], good: Good):
    for applicability_dir in applicability_list:
        model = handle_model(applicability_dir)
        if model:
            handle_applicability(model, good)


def handle_image_list(image_list: List[dir], good: Good):
    for image_dir in image_list:
        model = handle_model(image_dir)
        if model:
            handle_applicability(model, good)


def handle_good(good_dir: dir) -> Good:
    good_id = good_dir.get('id')
    good = good_by_id(good_id)
    if good is None:
        if good_id:
            good = Good.objects.create(id=good_id)
        else:
            good = Good.objects.create()

    good.name = good_dir.get('name', good.name)
    good.price = good_dir.get('price', good.price)
    good.balance = good_dir.get('balance', good.balance)
    good.art = good_dir.get('art', good.art)
    good.comment = good_dir.get('comment', good.comment)

    key_name = 'category'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        category = default_category()
        good.category = category if temp_dir is None else \
            handle_category(temp_dir)

    key_name = 'manufacturer'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.manufacturer = None if temp_dir is None else \
            handle_manufacturer(temp_dir)
    good.save()
    return good


def save_good_list_into_file(good_list: None) -> str:
    file_name = settings.BASE_DIR / "data.json"
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(good_list, file)
    return file_name


def load_good_list_from_file(file_name: str) -> bool:
    with open(file_name, "r", encoding="utf-8") as file:
        good_list = [item for item in json.loads(file.read())]
        # handle_good_list(good_list=good_list)
        thread = Thread(target=handle_good_list, args=[good_list])
        thread.start()
    return True


def handle_good_list(good_list: None) -> QuerySet[Good]:
    logger.info("start loading data.")
    goods_id = []
    with transaction.atomic():
        for good_item in good_list:
            good = handle_good(good_dir=good_item)

            key_name = 'applicability'
            if key_name in good_item:
                temp_dir = good_item.get(key_name)
                handle_applicability_list(temp_dir, good)

            key_name = 'images'
            if key_name in good_item:
                temp_dir = good_item.get(key_name)
                handle_image_list(temp_dir, good)

            goods_id.append(good.id)
    logger.info("finish loading data.")
    return Good.objects.filter(id__in=goods_id)


def fetch_goods_queryset_by_name_or_article(search: str) -> QuerySet[Good]:
    queryset = Good.objects.filter(
        Q(name__icontains=search) |
        Q(art__icontains=search)
        )
    return queryset


def fetch_goods_queryset_by_category(
        categories: List[Category]
        ) -> QuerySet[Good]:
    queryset = Good.objects.filter(category__in=categories)
    return queryset


def fetch_goods_queryset_by_manufacturer(
        manufacturers: List[Manufacturer]
        ) -> QuerySet[Good]:
    queryset = Good.objects.filter(manufacturer__in=manufacturers)
    return queryset


def fetch_goods_queryset_by_filters(
        categories: List[Category],
        manufacturers: List[Manufacturer]
        ) -> QuerySet[Good]:
    filters = Q()
    if categories:
        filters.add(Q(category__in=categories), Q.AND)

    if manufacturers:
        filters.add(Q(manufacturer__in=manufacturers), Q.AND)

    queryset = Good.objects.filter(filters)
    return queryset


def prepare_goods_to_serializing(queryset, user):
    @dataclass
    class CoupleOfGoodAndPrice:
        good: Good
        price: Decimal
    return [
        CoupleOfGoodAndPrice(
            good=record,
            price=current_price(record, user)
        ) for record in queryset
    ]
