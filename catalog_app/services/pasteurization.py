from django.db import transaction
from catalog_app.models import (
    Pasteurization
)


def pasteurization_by_id(pasteurization_id: str) -> Pasteurization:
    return Pasteurization.objects.filter(id=pasteurization_id).first()


def handle_pasteurization(pasteurization_dir: dir) -> Pasteurization:
    pasteurization_id = pasteurization_dir.get('id', "")
    pasteurization_name = pasteurization_dir.get('name', "")
    pasteurization = pasteurization_by_id(pasteurization_id)
    if pasteurization is None:
        pasteurization = Pasteurization.objects.create(
            id=pasteurization_id,
            name=pasteurization_name
        )
    return pasteurization


def handle_pasteurization_list(pasteurization_list: None) -> [Pasteurization]:
    pasteurization_id = []
    with transaction.atomic():
        for pasteurization_item in pasteurization_list:
            gassing = handle_pasteurization(
                pasteurization_dir=pasteurization_item)
            pasteurization_id.append(gassing.id)
    return Pasteurization.objects.filter(id__in=pasteurization_id)
