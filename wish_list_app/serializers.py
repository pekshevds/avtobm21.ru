from rest_framework import serializers
from catalog_app.serializers import GoodSerializer
# from auth_app.serializers import UserSerializer


class WishListSerializer(serializers.Serializer):
    # user = UserSerializer()
    good = GoodSerializer()


class SimpleWishListSerializer(serializers.Serializer):
    good_id = serializers.UUIDField()
