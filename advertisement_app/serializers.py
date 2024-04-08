from rest_framework import serializers
from image_app.serializers import ImageSerializer


class GroupOfPropertySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    ordering = serializers.DecimalField(
        max_digits=4, decimal_places=2, required=False)


class PropertySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    group = GroupOfPropertySerializer(required=False, allow_null=True)
    ordering = serializers.DecimalField(
        max_digits=4, decimal_places=2, required=False)


class AdvertisementsImageSerializer(serializers.Serializer):
    image = ImageSerializer(required=False, allow_null=True)


class ValuePropertyOfAnAdvertisementSerializer(serializers.Serializer):
    property = PropertySerializer()
    value = serializers.CharField(allow_blank=True)


class AdvertisementSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    price = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False)
    image = ImageSerializer(required=False, allow_null=True, read_only=True)
    description = serializers.CharField(allow_blank=True)
    images = AdvertisementsImageSerializer(required=False, allow_null=True,
                                           many=True, read_only=True)
    properties = ValuePropertyOfAnAdvertisementSerializer(
        required=False, allow_null=True, many=True, read_only=True)
