from django.db import transaction
from catalog_app.models import (
    Gassing
)


def gassing_by_id(gassing_id: str) -> Gassing:
    return Gassing.objects.filter(id=gassing_id).first()


def handle_gassing(gassing_dir: dir) -> Gassing:
    gassing_id = gassing_dir.get('id', "")
    gassing_name = gassing_dir.get('name', "")
    gassing = gassing_by_id(gassing_id)
    if gassing is None:
        gassing = Gassing.objects.create(
            id=gassing_id,
            name=gassing_name
        )
    return gassing


def handle_gassing_list(gassing_list: None) -> [Gassing]:
    gassing_id = []
    with transaction.atomic():
        for category_item in gassing_list:
            gassing = handle_gassing(gassing_dir=category_item)
            gassing_id.append(gassing.id)
    return Gassing.objects.filter(id__in=gassing_id)
