from django.http import HttpRequest
from rest_framework import (
    permissions,
    authentication
)
from rest_framework.views import APIView
from rest_framework.response import Response
from price_app.models import (
    KindPrice,
    Price
)
from price_app.serializers import (
    KindPriceSerializer,
    SiplePriceSerializer
)
from catalog_app.models import Good


class KindPriceView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> Response:
        queryset = KindPrice.objects.all()
        serializer = KindPriceSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "count": len(queryset),
                    "success": True}
        return Response(response)

    def post(self, request: HttpRequest) -> Response:
        response = {"data": [],
                    "count": 0,
                    "success": False}
        data = request.data.get("data", None)
        if not data:
            return Response(response)
        serializer = KindPriceSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer.data
            response["count"] = len(serializer.data)
            response["success"] = True
        return Response(response)


class PriceView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id", 0)
        if id:
            good = Good.objects.filter(id=id).first()
            queryset = None
            if good:
                queryset = Price.objects.filter(good=good)
            serializer = SiplePriceSerializer(queryset, many=True)
        else:
            queryset = Price.objects.all()
            serializer = SiplePriceSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "count": len(serializer.data),
                    "success": True}
        return Response(response)

    def post(self, request: HttpRequest) -> Response:
        response = {"data": [],
                    "count": 0,
                    "success": False}
        data = request.data.get("data", None)
        if not data:
            return Response(response)
        serializer = SiplePriceSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer.data
            response["count"] = len(serializer.data)
            response["success"] = True
        return Response(response)
