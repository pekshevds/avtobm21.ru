from typing import List
from django.db import transaction
from catalog_app.models import (
    Manufacturer
)


def manufacturer_by_id(id: str) -> Manufacturer:
    return Manufacturer.objects.filter(id=id).first()


def manufacturer_by_id_list(id: List[str]) -> List[Manufacturer]:
    return list(Manufacturer.objects.filter(id__in=id))


def handle_manufacturer(item_dir: dir) -> Manufacturer:
    item_id = item_dir.get('id', None)
    item = manufacturer_by_id(id=item_id)
    if item is None:
        if item_id:
            item = Manufacturer.objects.create(id=item_id)
        else:
            item = Manufacturer.objects.create()
    item.name = item_dir.get('name', item.name)
    item.save()
    return item


def handle_manufacturer_list(item_list: List[dir]) -> List[Manufacturer]:
    items_id = []
    with transaction.atomic():
        for item_dir in item_list:
            item = handle_manufacturer(item_dir=item_dir)
            items_id.append(item.id)
    return Manufacturer.objects.filter(id__in=items_id)
