from django.db import transaction
from catalog_app.models import (
    Filtering
)


def filtering_by_id(filtering_id: str) -> Filtering:
    return Filtering.objects.filter(id=filtering_id).first()


def handle_filtering(filtering_dir: dir) -> Filtering:
    filtering_id = filtering_dir.get('id', "")
    filtering_name = filtering_dir.get('name', "")
    filtering = filtering_by_id(filtering_id)
    if filtering is None:
        filtering = Filtering.objects.create(
            id=filtering_id,
            name=filtering_name
        )
    return filtering


def handle_filtering_list(filtering_list: None) -> [Filtering]:
    filtering_id = []
    with transaction.atomic():
        for filtering_item in filtering_list:
            filtering = handle_filtering(filtering_dir=filtering_item)
            filtering_id.append(filtering.id)
    return Filtering.objects.filter(id__in=filtering_id)
