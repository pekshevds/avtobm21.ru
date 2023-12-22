from django.db import transaction
from catalog_app.models import (
    Category
)


def category_by_id(id: str) -> Category:
    return Category.objects.filter(id=id).first()


def category_by_id_list(id: [str]) -> [Category]:
    return list(Category.objects.filter(id__in=id))


def handle_category(item_dir: dir) -> Category:
    item_id = item_dir.get('id', "")
    item = category_by_id(id=item_id)
    if item is None:
        item = Category.objects.create(
            id=item_id
        )
    item.name = item_dir.get('name', item.name)
    item.save()
    return item


def handle_category_list(item_list: [dir]) -> [Category]:
    items_id = []
    with transaction.atomic():
        for item_dir in item_list:
            item = handle_category(item_dir=item_dir)
            items_id.append(item.id)
    return Category.objects.filter(id__in=items_id)
