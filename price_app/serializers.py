from rest_framework import serializers
from catalog_app.serializers import GoodSerializer
from catalog_app.models import Good
from price_app.models import (
    KindPrice,
    Price
)


class KindPriceSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)

    def create(self, validated_data):
        id = validated_data["id"]
        name = validated_data["name"]
        record, _ = KindPrice.objects.get_or_create(id=id)
        record.name = name
        record.save()
        return record


class SiplePriceSerializer(serializers.Serializer):
    kind_id = serializers.UUIDField()
    good_id = serializers.UUIDField()
    price = serializers.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    def create(self, validated_data):
        kind_id = validated_data["kind_id"]
        good_id = validated_data["good_id"]
        price = validated_data["price"]
        kind = KindPrice.objects.get(id=kind_id)
        good = Good.objects.get(id=good_id)
        record, _ = Price.objects.get_or_create(kind=kind, good=good)
        record.price = price
        record.save()
        return record


class PriceSerializer(serializers.Serializer):
    kind = KindPriceSerializer()
    good = GoodSerializer()
    price = serializers.DecimalField(
        max_digits=15,
        decimal_places=2
    )
