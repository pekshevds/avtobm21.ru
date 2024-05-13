import logging
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication
from order_app.models import (
    Contract,
    Order,
    ItemOrder,
    OrderStatus
)
from order_app.serializers import (
    ContractSerializer,
    SimpleOrderSerializer,
    OrderSerializer,
    ItemOrderSerializer,
    SimpleItemOrderSerializer,
    OrderStatusSerializer
)
from order_app.services.order import (
    handle_order_list,
    order_by_id,
    status_by_value,
    put_order_status,
    new_orders,
    handle_order_status_list
)

logger = logging.getLogger(__name__)
default_number_of_page = 1
item_count_per_page = 5


class OrderStatusView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest) -> Response:
        queryset = OrderStatus.objects.all()
        serializer = OrderStatusSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "count": len(queryset),
                    "success": True}
        return Response(response)


class ContractView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest) -> Response:
        client = request.user.client
        queryset = Contract.objects.filter(client=client)
        serializer = ContractSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "count": len(queryset),
                    "success": True}
        return Response(response)


class PutOrderStatusView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest) -> Response:
        order = order_by_id(order_id=request.GET.get("id"))
        status = status_by_value(request.GET.get("value"))
        success = False
        if order and status:
            success = put_order_status(order, status)
        response = {"data": [],
                    "count": 0,
                    "success": success}
        return Response(response)

    def post(self, request: HttpRequest) -> Response:
        response = {"data": [],
                    "count": 0,
                    "success": False}
        data = request.data.get("data")
        if not data:
            return Response(response)
        handle_order_status_list(data)
        response["success"] = True
        return Response(response)


class NewOrdersView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest) -> Response:
        queryset = new_orders()
        serializer = OrderSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "count": len(queryset),
                    "success": True}
        return Response(response)


class OrderView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest) -> Response:
        client = request.user.client
        order = order_by_id(order_id=request.GET.get("id"))
        if order:
            queryset = [order]
        else:
            page_number = request.GET.get("page", default_number_of_page)
            count = request.GET.get("count", item_count_per_page)

            queryset = Order.objects.filter(client=client)
            paginator = Paginator(queryset, count)
            queryset = paginator.get_page(page_number)
        serializer = OrderSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "count": len(queryset),
                    "success": True}
        return Response(response)

    def post(self, request: HttpRequest) -> Response:
        response = {"data": [],
                    "count": 0,
                    "success": False}
        data = request.data.get("data")
        if not data:
            return Response(response)
        logger.info(data)
        serializer = SimpleOrderSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            queryset = handle_order_list(order_list=data, author=request.user)
            paginator = Paginator(queryset, default_number_of_page)
            queryset = paginator.get_page(item_count_per_page)
            serializer = OrderSerializer(queryset, many=True)
            response["data"] = serializer.data
            response["count"] = len(queryset)
            response["success"] = True
        return Response(response)


class OrderDeleteView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest) -> Response:
        order = get_object_or_404(Order, id=request.GET.get("id"))
        order.delete()
        response = {"data": [],
                    "success": True}
        return Response(response)


class OrderItemView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest) -> Response:
        order = get_object_or_404(Order, id=request.GET.get("id"))
        serializer = SimpleItemOrderSerializer(order.items, many=True)
        response = {"data": serializer.data,
                    "count": len(serializer.data),
                    "success": True}
        return Response(response)


class OrderItemDeleteView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest) -> Response:
        item = get_object_or_404(ItemOrder, id=request.GET.get("id"))
        order = item.order
        item.delete()
        serializer = ItemOrderSerializer(order.items, many=True)
        response = {"data": serializer.data,
                    "count": len(serializer.data),
                    "success": True}
        return Response(response)
