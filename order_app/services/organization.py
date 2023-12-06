from django.db import transaction
from order_app.models import (
    Organization
)


def organization_by_id(organization_id: str) -> Organization:
    return Organization.objects.filter(id=organization_id).first()


def handle_organization(organization_dir: dir) -> Organization:
    organization_id = organization_dir.get('id', None)
    organization_name = organization_dir.get('name', "")
    organization_inn = organization_dir.get('inn', "")
    organization = organization_by_id(organization_id)
    if organization is None:
        organization = Organization.objects.create(
            id=organization_id,
            name=organization_name
        )
    organization.name = organization_name
    organization.inn = organization_inn
    organization.save()
    return organization


def handle_organization_list(organization_list: None) -> [Organization]:
    organization_id = []
    with transaction.atomic():
        for organization_item in organization_list:
            organization = handle_organization(
                organization_dir=organization_item
            )
            organization_id.append(organization.id)
    return Organization.objects.filter(id__in=organization_id)
