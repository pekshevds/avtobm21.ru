from rest_framework import serializers
from order_app.serializers import ClientSerializer


class UserSerializer(serializers.Serializer):
    client = ClientSerializer()
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    is_active = serializers.BooleanField()
