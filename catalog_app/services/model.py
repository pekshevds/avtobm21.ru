from django.db import transaction
from catalog_app.models import (
    Model
)


def model_by_id(id: str) -> Model:
    return Model.objects.filter(id=id).first()


def handle_model(item_dir: dir) -> Model:
    item_id = item_dir.get('id', "")
    item = model_by_id(id=item_id)
    if item is None:
        item = Model.objects.create(
            id=item_id
        )
    item.name = item_dir.get('name', item.name)
    item.save()
    return item


def handle_model_list(item_list: [dir]) -> [Model]:
    items_id = []
    with transaction.atomic():
        for item_dir in item_list:
            item = handle_model(item_dir=item_dir)
            items_id.append(item.id)
    return Model.objects.filter(id__in=items_id)
