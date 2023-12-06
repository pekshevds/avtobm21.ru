from django.db import transaction
from order_app.models import (
    Client
)


def client_by_id(client_id: str) -> Client:
    return Client.objects.filter(id=client_id).first()


def handle_client(client_dir: dir) -> Client:
    client_id = client_dir.get('id', None)
    client_name = client_dir.get('name', "")
    client = client_by_id(client_id)
    if client is None:
        client = Client.objects.create(
            id=client_id,
            name=client_name
        )
    client.name = client_name
    client.save()
    return client


def handle_client_list(client_list: None) -> [Client]:
    client_id = []
    with transaction.atomic():
        for client_item in client_list:
            client = handle_client(client_dir=client_item)
            client_id.append(client.id)
    return Client.objects.filter(id__in=client_id)
