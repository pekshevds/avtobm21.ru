from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication
from catalog_app.models import Good

from cart_app.serializers import CartSerializer
from cart_app.services import (
    fetch_users_cart,
    add_to_cart,
    delete_from_cart,
    clear_cart
)


class CartView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest) -> Response:
        queryset = fetch_users_cart(request.user)
        serializer = CartSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "success": True}
        return Response(response)


class CartAddView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest) -> Response:
        good = get_object_or_404(Good, id=request.GET.get("good_id"))
        add_to_cart(user=request.user, good=good)

        queryset = fetch_users_cart(request.user)
        serializer = CartSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "success": True}
        return Response(response)

    def post(self, request: HttpRequest) -> Response:
        response = {"data": [],
                    "success": False}
        data = request.data.get("data")
        if not data:
            return Response(response)
        for item in data:
            good_id = item.get("good_id")
            quantity = item.get("quantity", 0)
            good = get_object_or_404(Good, id=good_id)
            add_to_cart(user=request.user, good=good, quantity=quantity)

        queryset = fetch_users_cart(request.user)
        serializer = CartSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "success": True}
        return Response(response)


class CartDeleteView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest) -> Response:
        good = get_object_or_404(Good, id=request.GET.get("good_id"))
        delete_from_cart(user=request.user, good=good)

        queryset = fetch_users_cart(request.user)
        serializer = CartSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "success": True}
        return Response(response)

    def post(self, request: HttpRequest) -> Response:
        response = {"data": [],
                    "success": False}
        data = request.data.get("data")
        if not data:
            return Response(response)
        for item in data:
            good_id = item.get("good_id")
            quantity = item.get("quantity", 0)
            good = get_object_or_404(Good, id=good_id)
            delete_from_cart(user=request.user, good=good, quantity=quantity)

        queryset = fetch_users_cart(request.user)
        serializer = CartSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "success": True}
        return Response(response)


class CartClearView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest) -> Response:
        clear_cart(user=request.user)

        queryset = fetch_users_cart(request.user)
        serializer = CartSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "success": True}
        return Response(response)
