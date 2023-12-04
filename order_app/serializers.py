from rest_framework import serializers
from catalog_app.serializers import GoodSerializer


class ClientSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)


class CustomerSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    inn = serializers.CharField(max_length=12)


class OrganizationSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    inn = serializers.CharField(max_length=12)


class ContractSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    number = serializers.CharField(max_length=25)
    date = serializers.DateField(format='%Y-%m-%d')
    client = ClientSerializer()
    customer = CustomerSerializer()
    organization = OrganizationSerializer()


class ItemOrderSerializer(serializers.Serializer):
    good = GoodSerializer()
    quantity = serializers.DecimalField(max_digits=15, decimal_places=3)
    price = serializers.DecimalField(max_digits=15, decimal_places=2)
    summ = serializers.DecimalField(max_digits=15, decimal_places=2)


class OrderSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    number = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField(format='%Y-%m-%d')
    contract = ContractSerializer()
    items = ItemOrderSerializer(many=True)
