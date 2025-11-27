from rest_framework import serializers


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    date = serializers.CharField(max_length=10)
    free_hours = serializers.IntegerField(default=0)
    total_hour = serializers.IntegerField(default=0)


class DataSerializer(serializers.Serializer):
    posts = ItemSerializer(allow_null=True, many=True)
    workers = ItemSerializer(allow_null=True, many=True)


class BodySerializer(serializers.Serializer):
    auth = AuthSerializer()
    data = DataSerializer()
