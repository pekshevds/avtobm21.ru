from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)


class ModelSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)


class ManufacturerSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)


class GoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    art = serializers.CharField(
        max_length=25, required=False, allow_blank=True)
    balance = serializers.DecimalField(
        max_digits=15, decimal_places=3, required=False)
    price = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False)
    code_okdp2 = CategorySerializer(required=False, allow_null=True)
    model = ModelSerializer(required=False, allow_null=True)
    manufacturer = ManufacturerSerializer(required=False, allow_null=True)


class SimpleGoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    art = serializers.CharField(
        max_length=25, required=False, allow_blank=True)
    balance = serializers.DecimalField(
        max_digits=15, decimal_places=3, required=False)
    price = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False)
    category_id = serializers.UUIDField(required=False, allow_null=True)
    manufacturer_id = serializers.UUIDField(required=False, allow_null=True)