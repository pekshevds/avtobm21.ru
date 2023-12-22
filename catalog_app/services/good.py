from django.db.models import Q
from django.db import transaction
from catalog_app.models import (
    Good,
    Model,
    Applicability,
    Category,
    Manufacturer
)
from catalog_app.services.category import handle_category
from catalog_app.services.manufacturer import handle_manufacturer
from catalog_app.services.model import handle_model


def good_by_id(good_id: str) -> Good:
    return Good.objects.filter(id=good_id).first()


def handle_applicability(model: Model, good: Good) -> None:
    applicability = Applicability.objects.filter(
        model=model, good=good
    ).first()
    if not applicability:
        applicability = Applicability.objects.create(
            model=model,
            good=good
        )
    return applicability


def handle_applicability_list(applicability_list: [dir], good: Good):
    for applicability_dir in applicability_list:
        model = handle_model(applicability_dir)
        if model:
            handle_applicability(model, good)


def handle_image_list(image_list: [dir], good: Good):
    for image_dir in image_list:
        model = handle_model(image_dir)
        if model:
            handle_applicability(model, good)


def handle_good(good_dir: dir) -> Good:
    good_id = good_dir.get('id', None)
    good = good_by_id(good_id)
    if good is None:
        good = Good.objects.create(
            id=good_id,
        )
    good.name = good_dir.get('name', good.name)
    good.price = good_dir.get('price', good.price)
    good.balance = good_dir.get('balance', good.balance)
    good.art = good_dir.get('art', good.art)
    good.comment = good_dir.get('comment', good.comment)

    key_name = 'category'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.category = None if temp_dir is None else \
            handle_category(temp_dir)

    key_name = 'manufacturer'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.manufacturer = None if temp_dir is None else \
            handle_manufacturer(temp_dir)
    good.save()
    return good


def handle_good_list(good_list: None) -> [Good]:
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

    return Good.objects.filter(id__in=goods_id)


def fetch_goods_queryset_by_name_or_article(search: str):
    queryset = Good.objects.filter(
        Q(name__icontains=search) |
        Q(art__icontains=search)
        )
    return queryset


def fetch_goods_queryset_by_category(categories: [Category]):
    queryset = Good.objects.filter(category__in=categories)
    return queryset


def fetch_goods_queryset_by_manufacturer(manufacturers: [Manufacturer]):
    queryset = Good.objects.filter(manufacturer__in=manufacturers)
    return queryset


def fetch_goods_queryset_by_filters(
        categories: [Category],
        manufacturers: [Manufacturer]
        ):
    filters = Q()
    if categories:
        filters.add(Q(category__in=categories), Q.AND)

    if manufacturers:
        filters.add(Q(manufacturer__in=manufacturers), Q.AND)

    queryset = Good.objects.filter(filters)
    return queryset
