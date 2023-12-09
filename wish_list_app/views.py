from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication
from catalog_app.models import Good

from wish_list_app.serializers import WishListSerializer
from wish_list_app.services import (
    fetch_users_wish_list,
    add_to_wish_list,
    delete_from_wish_list,
    clear_wish_list
)


class WishListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        queryset = fetch_users_wish_list(request.user)
        serializer = WishListSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class WishListAddView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        good = get_object_or_404(Good, id=request.GET.get("good_id", None))
        add_to_wish_list(user=request.user, good=good)

        queryset = fetch_users_wish_list(request.user)
        serializer = WishListSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class WishListDeleteView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        good = get_object_or_404(Good, id=request.GET.get("good_id", None))
        delete_from_wish_list(user=request.user, good=good)

        queryset = fetch_users_wish_list(request.user)
        serializer = WishListSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class WishListClearView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        clear_wish_list(user=request.user)

        queryset = fetch_users_wish_list(request.user)
        serializer = WishListSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)
