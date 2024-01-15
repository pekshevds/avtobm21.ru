from rest_framework import serializers
from image_app.serializers import ImageSerializer


class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)


class ModelSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)


class ManufacturerSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)


class GoodsImageSerializer(serializers.Serializer):
    image = ImageSerializer(required=False, allow_null=True)


class GoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    art = serializers.CharField(
        max_length=50, required=False, allow_blank=True)
    balance = serializers.DecimalField(
        max_digits=15, decimal_places=3, required=False)
    price = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False)
    category = CategorySerializer(required=False, allow_null=True)
    manufacturer = ManufacturerSerializer(required=False, allow_null=True)
    preview = ImageSerializer(required=False, allow_null=True,
                              source="image", read_only=True)
    images = GoodsImageSerializer(required=False, allow_null=True,
                                  many=True, read_only=True)


class SimpleGoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    art = serializers.CharField(
        max_length=50, required=False, allow_blank=True)
    balance = serializers.DecimalField(
        max_digits=15, decimal_places=3, required=False)
    price = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False)
    category_id = serializers.UUIDField(required=False, allow_null=True)
    manufacturer_id = serializers.UUIDField(required=False, allow_null=True)
    preview = ImageSerializer(required=False, allow_null=True,
                              source="image", read_only=True)
    images = GoodsImageSerializer(required=False, allow_null=True,
                                  many=True, read_only=True)
