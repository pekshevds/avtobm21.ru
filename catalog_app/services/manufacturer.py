from django.db import transaction
from catalog_app.models import (
    Manufacturer
)


def manufacturer_by_id(manufacturer_id: str) -> Manufacturer:
    return Manufacturer.objects.filter(id=manufacturer_id).first()


def handle_manufacturer(manufacturer_dir: dir) -> Manufacturer:
    manufacturer_id = manufacturer_dir.get('id', "")
    manufacturer_name = manufacturer_dir.get('name', "")
    manufacturer = manufacturer_by_id(manufacturer_id)
    if manufacturer is None:
        manufacturer = Manufacturer.objects.create(
            id=manufacturer_id,
            name=manufacturer_name
        )
    return manufacturer


def handle_manufacturer_list(manufacturer_list: None) -> [Manufacturer]:
    manufacturer_id = []
    with transaction.atomic():
        for manufacturer_item in manufacturer_list:
            manufacturer = handle_manufacturer(
                manufacturer_dir=manufacturer_item
            )
            manufacturer_id.append(manufacturer.id)
    return Manufacturer.objects.filter(id__in=manufacturer_id)
