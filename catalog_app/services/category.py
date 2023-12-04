from django.db import transaction
from catalog_app.models import (
    Category
)


def category_by_id(id: str) -> Category:
    return Category.objects.filter(id=id).first()


def handle_category(category_dir: dir) -> Category:
    category_id = category_dir.get('id', "")
    category_name = category_dir.get('name', "")
    category = category_by_id(category_id)
    if category is None:
        category = Category.objects.create(
            id=category_id,
            name=category_name
        )
    return category


def handle_category_list(category_list: None) -> [Category]:
    categories_id = []
    with transaction.atomic():
        for category_item in category_list:
            category = handle_category(category_dir=category_item)
            categories_id.append(category.id)
    return Category.objects.filter(id__in=categories_id)
