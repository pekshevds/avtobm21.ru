from django.shortcuts import get_object_or_404
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


class OrderStatusView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        queryset = OrderStatus.objects.all()
        serializer = OrderStatusSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "success": True}
        return Response(response)


class ContractView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        client = request.user.client
        queryset = Contract.objects.filter(client=client)
        serializer = ContractSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "success": True}
        return Response(response)


class PutOrderStatusView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        order = order_by_id(order_id=request.GET.get("id"))
        status = status_by_value(request.GET.get("value"))
        success = False
        if order and status:
            success = put_order_status(order, status)
        response = {"data": [],
                    "success": success}
        return Response(response)

    def post(self, request):
        response = {"data": [],
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

    def get(self, request):
        queryset = new_orders()
        serializer = OrderSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "success": True}
        return Response(response)


class OrderView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        client = request.user.client
        order = order_by_id(order_id=request.GET.get("id"))
        if order:
            queryset = [order]
        else:
            queryset = Order.objects.filter(client=client)
        serializer = OrderSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "success": True}
        return Response(response)

    def post(self, request):
        response = {"data": [],
                    "success": False}
        data = request.data.get("data")
        if not data:
            return Response(response)
        serializer = SimpleOrderSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            queryset = handle_order_list(order_list=data, author=request.user)
            serializer = OrderSerializer(queryset, many=True)
            response["data"] = serializer.data
            response["success"] = True
        return Response(response)


class OrderDeleteView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        order = get_object_or_404(Order, id=request.GET.get("id"))
        order.delete()
        response = {"data": [],
                    "success": True}
        return Response(response)


class OrderItemView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        order = get_object_or_404(Order, id=request.GET.get("id"))
        serializer = SimpleItemOrderSerializer(order.items, many=True)
        response = {"data": serializer.data,
                    "success": True}
        return Response(response)


class OrderItemDeleteView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        item = get_object_or_404(ItemOrder, id=request.GET.get("id"))
        order = item.order
        item.delete()
        serializer = ItemOrderSerializer(order.items, many=True)
        response = {"data": serializer.data,
                    "success": True}
        return Response(response)
