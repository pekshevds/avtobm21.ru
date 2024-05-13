from django.http import HttpRequest
from django.core.paginator import Paginator
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
    # handle_good_list,
    save_good_list_into_file,
    load_good_list_from_file,
    fetch_goods_queryset_by_name_or_article
)
from catalog_app.services.category import category_by_id_list
from catalog_app.services.manufacturer import manufacturer_by_id_list
from catalog_app.services.good import fetch_goods_queryset_by_filters


class ManufacturerView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id")
        if id:
            queryset = Manufacturer.objects.filter(id=id)
            serializer = ManufacturerSerializer(queryset, many=True)
        else:
            queryset = Manufacturer.objects.all()
            serializer = ManufacturerSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "count": len(queryset),
                    "success": True}
        return Response(response)


class ModelView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id", 0)
        if id:
            queryset = Model.objects.filter(id=id)
            serializer = ModelSerializer(queryset, many=True)
        else:
            queryset = Model.objects.all()
            serializer = ModelSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "count": len(queryset),
                    "success": True}
        return Response(response)


class CategoryView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id", 0)
        if id:
            queryset = Category.objects.filter(id=id)
            serializer = CategorySerializer(queryset, many=True)
        else:
            queryset = Category.objects.all()
            serializer = CategorySerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "count": len(queryset),
                    "success": True}
        return Response(response)


class GoodView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> Response:
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
            else:

                categories = None
                category_id = request.GET.get("category_id")
                if category_id:
                    categories = category_by_id_list(category_id.split(","))

                manufacturers = None
                manufacturer_id = request.GET.get("manufacturer_id")
                if manufacturer_id:
                    manufacturers = manufacturer_by_id_list(
                        manufacturer_id.split(",")
                    )
                queryset = fetch_goods_queryset_by_filters(
                    categories,
                    manufacturers
                )

            if queryset is None:
                queryset = Good.objects.all()

            paginator = Paginator(queryset, count)
            serializer = GoodSerializer(
                paginator.get_page(page_number), many=True
            )
        response = {
            "data": serializer.data,
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
        serializer = GoodSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            # queryset = handle_good_list(good_list=data)
            # queryset = handle_good_list(good_list=[item for item in data])
            # serializer = GoodSerializer(queryset, many=True)
            # response["data"] = serializer.data

            file_name = save_good_list_into_file(good_list=data)
            load_good_list_from_file(file_name=file_name)
            response["success"] = True
        return Response(response)
