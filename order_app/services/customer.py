from django.db import transaction
from order_app.models import (
    Customer
)


def customer_by_id(customer_id: str) -> Customer:
    return Customer.objects.filter(id=customer_id).first()


def handle_customer(customer_dir: dir) -> Customer:
    customer_id = customer_dir.get('id', None)
    customer_name = customer_dir.get('name', "")
    customer_inn = customer_dir.get('inn', "")
    customer = customer_by_id(customer_id)
    if customer is None:
        customer = Customer.objects.create(
            id=customer_id,
            name=customer_name
        )
    customer.name = customer_name
    customer.inn = customer_inn
    customer.save()
    return customer


def handle_customer_list(customer_list: None) -> [Customer]:
    customer_id = []
    with transaction.atomic():
        for customer_item in customer_list:
            customer = handle_customer(customer_dir=customer_item)
            customer_id.append(customer.id)
    return Customer.objects.filter(id__in=customer_id)
