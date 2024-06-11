from rest_framework import serializers
from catalog_app.serializers import GoodSerializer
# from auth_app.serializers import UserSerializer


class WishListSerializer(serializers.Serializer):
    # user = UserSerializer()
    good = GoodSerializer()
    price = serializers.DecimalField(
        max_digits=15, decimal_places=2, allow_null=True, read_only=True
    )


class SimpleWishListSerializer(serializers.Serializer):
    good_id = serializers.UUIDField()
    price = serializers.DecimalField(
        max_digits=15, decimal_places=2, allow_null=True, read_only=True
    )
