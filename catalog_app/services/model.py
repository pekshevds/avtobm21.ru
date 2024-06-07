from typing import List
from django.db import transaction
from django.db.models.query import QuerySet
from catalog_app.models import (
    Model
)


def model_by_id(id: str) -> Model:
    return Model.objects.filter(id=id).first()


def handle_model(item_dir: dir) -> Model:
    obj, _ = Model.objects.get_or_create(id=item_dir.get("id"))
    obj.name = item_dir.get("name", obj.name)
    obj.save()
    return obj


def handle_model_list(item_list: List[dir]) -> QuerySet[Model]:
    items_id = []
    with transaction.atomic():
        for item_dir in item_list:
            item = handle_model(item_dir=item_dir)
            items_id.append(item.id)
    return Model.objects.filter(id__in=items_id)
