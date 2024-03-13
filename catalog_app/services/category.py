
from typing import List
from django.db import transaction
from catalog_app.models import (
    Category
)


def default_category() -> Category:
    return Category.objects.filter(name="Прочее").first()


def category_by_id(id: str) -> Category:
    return Category.objects.filter(id=id).first()


def category_by_id_list(id: List[str]) -> List[Category]:
    return list(Category.objects.filter(id__in=id))


def handle_category(item_dir: dir) -> Category:
    item_id = item_dir.get('id', None)
    item = category_by_id(id=item_id)
    if item is None:
        if item_id:
            item = Category.objects.create(id=item_id)
        else:
            item = Category.objects.create()
    item.name = item_dir.get('name', item.name)
    item.save()
    return item


def handle_category_list(item_list: List[dir]) -> List[Category]:
    items_id = []
    with transaction.atomic():
        for item_dir in item_list:
            item = handle_category(item_dir=item_dir)
            items_id.append(item.id)
    return Category.objects.filter(id__in=items_id)
