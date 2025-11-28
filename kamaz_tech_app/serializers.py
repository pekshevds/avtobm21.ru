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


class LoadServicesIncomingSerializer(serializers.Serializer):
    auth = AuthSerializer()
    data = DataSerializer()


class StatusSerializer(serializers.Serializer):
    order_id = serializers.CharField(max_length=36)
    order_status = serializers.CharField(max_length=36)
    order_comment = serializers.CharField(
        max_length=1024, required=False, allow_blank=True
    )
    handling_reason = serializers.CharField(
        max_length=1024, required=False, allow_blank=True
    )
    dealer_comment = serializers.CharField(max_length=1024, required=True)


class OrderServiceStatusIncomingSerializer(serializers.Serializer):
    auth = AuthSerializer()
    data = StatusSerializer()


class AuthIncomingSerializer(serializers.Serializer):
    auth = AuthSerializer()
