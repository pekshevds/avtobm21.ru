from typing import Any
from django.http import HttpRequest
from rest_framework import permissions, authentication, status
from rest_framework.views import APIView
from rest_framework.response import Response
from kamaz_tech_app.serializers import (
    LoadServicesIncomingSerializer,
    AuthSerializer,
    OrderServiceStatusSerializer,
)
from kamaz_tech_app.utils import (
    get_auth_token,
    upload_services,
    download_orders,
    update_orders_status,
)


class LoadServicesView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request: HttpRequest) -> Response:
        serialiser = LoadServicesIncomingSerializer(data=request.data)
        if not serialiser.is_valid():
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serialiser.validated_data
        auth = validated_data.get("auth")
        data = validated_data.get("data")
        token = get_auth_token(auth.get("username"), auth.get("password"))
        if token:
            return Response(upload_services(token, data))
        response: dict[str, Any] = {}
        return Response(response)


class OrderServicesView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> Response:
        serialiser = AuthSerializer(data=request.data)
        if not serialiser.is_valid():
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serialiser.validated_data
        token = get_auth_token(
            validated_data.get("username"), validated_data.get("password")
        )
        if token:
            return Response(download_orders(token))
        response: dict[str, Any] = {}
        return Response(response)

    def post(self, request: HttpRequest) -> Response:
        serialiser = OrderServiceStatusSerializer(data=request.data)
        if not serialiser.is_valid():
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serialiser.validated_data
        auth = validated_data.get("auth")
        data = validated_data.get("data")
        token = get_auth_token(auth.get("username"), auth.get("password"))
        if token:
            return Response(update_orders_status(token, data))
        response: dict[str, Any] = {}
        return Response(response)
