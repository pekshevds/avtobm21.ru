from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from rest_framework import (
    permissions,
    authentication
)
from rest_framework.views import APIView
from rest_framework.response import Response
from catalog_app.models import (
    Manufacturer,
    Model,
    Category,
    Good
)
from catalog_app.serializers import (
    ManufacturerSerializer,
    ModelSerializer,
    GoodSerializer,
    CategorySerializer
)
from catalog_app.services.good import (
    handle_good_list,
    fetch_goods_queryset_by_name_or_article,
    fetch_goods_queryset_by_category,
    fetch_goods_queryset_by_manufacturer
)


class ManufacturerView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        id = request.GET.get("id")
        if id:
            queryset = Manufacturer.objects.filter(id=id)
            serializer = ManufacturerSerializer(queryset, many=True)
        else:
            queryset = Manufacturer.objects.all()
            serializer = ManufacturerSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class ModelView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        id = request.GET.get("id", 0)
        if id:
            queryset = Model.objects.filter(id=id)
            serializer = ModelSerializer(queryset, many=True)
        else:
            queryset = Model.objects.all()
            serializer = ModelSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class CategoryView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        id = request.GET.get("id", 0)
        if id:
            queryset = Category.objects.filter(id=id)
            serializer = CategorySerializer(queryset, many=True)
        else:
            queryset = Category.objects.all()
            serializer = CategorySerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class GoodView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        id = request.GET.get("id", 0)
        if id:
            queryset = Good.objects.filter(id=id)
            serializer = GoodSerializer(queryset, many=True)
        else:
            page_number = request.GET.get("page", 1)
            count = request.GET.get("count", 25)
            queryset = None

            search = request.GET.get("search")
            if search:
                queryset = fetch_goods_queryset_by_name_or_article(search)

            category_id = request.GET.get("category_id")
            if category_id:
                category = get_object_or_404(Category, pk=category_id)
                queryset = fetch_goods_queryset_by_category(category)

            manufacturer_id = request.GET.get("manufacturer_id")
            if manufacturer_id:
                manufacturer = get_object_or_404(
                    Manufacturer, pk=manufacturer_id
                )
                queryset = fetch_goods_queryset_by_manufacturer(manufacturer)

            if queryset is None:
                queryset = Good.objects.all()

            paginator = Paginator(queryset, count)
            serializer = GoodSerializer(
                paginator.get_page(page_number), many=True
            )
        response = {
            "data": serializer.data,
            "count": len(queryset)
            }
        return Response(response)

    def post(self, request):
        response = {"data": []}
        data = request.data.get("data", None)
        if not data:
            return Response(response)
        serializer = GoodSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            queryset = handle_good_list(good_list=data)
            serializer = GoodSerializer(queryset, many=True)
            response["data"] = serializer.data
        return Response(response)
