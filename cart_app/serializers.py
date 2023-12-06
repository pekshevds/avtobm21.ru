from rest_framework import serializers
from catalog_app.serializers import GoodSerializer
# from auth_app.serializers import UserSerializer


class CartSerializer(serializers.Serializer):
    # user = UserSerializer()
    good = GoodSerializer()
    quantity = serializers.DecimalField(max_digits=15, decimal_places=3)


class SimpleCartSerializer(serializers.Serializer):
    good_id = serializers.UUIDField()
    quantity = serializers.DecimalField(max_digits=15, decimal_places=3)
