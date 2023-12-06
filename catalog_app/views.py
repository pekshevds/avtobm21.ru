from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework import permissions, authentication
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
from catalog_app.services.good import handle_good_list


class ManufacturerView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

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

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

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

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

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
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        id = request.GET.get("id", 0)
        if id:
            queryset = Good.objects.filter(id=id)
            serializer = GoodSerializer(queryset, many=True)
        else:
            page_number = request.GET.get("page", 1)
            count = request.GET.get("count", 25)
            filter = request.GET.get("filter")
            if filter:
                queryset = Good.objects.filter(
                    Q(name__icontains=filter) |
                    Q(art__icontains=filter)
                    )
            else:
                queryset = Good.objects.all()
            paginator = Paginator(queryset, count)
            serializer = GoodSerializer(
                paginator.get_page(page_number), many=True
            )
        response = {"data": serializer.data}
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
