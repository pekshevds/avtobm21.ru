from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication
from order_app.models import (
    Contract,
    Order,
    ItemOrder
)
from order_app.serializers import (
    ContractSerializer,
    SimpleOrderSerializer,
    OrderSerializer,
    ItemOrderSerializer,
    SimpleItemOrderSerializer
)
from order_app.services.order import handle_order_list


class ContractView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        client = request.user.client
        queryset = Contract.objects.filter(client=client)
        serializer = ContractSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class OrderView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        client = request.user.client
        order_id = request.GET.get("id", None)
        if order_id:
            queryset = Order.objects.filter(id=order_id, client=client)
        else:
            queryset = Order.objects.filter(client=client)
        serializer = OrderSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)

    def post(self, request):
        response = {"data": []}
        data = request.data.get("data", None)
        if not data:
            return Response(response)
        serializer = SimpleOrderSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            queryset = handle_order_list(order_list=data)
            serializer = OrderSerializer(queryset, many=True)
            response["data"] = serializer.data
        return Response(response)


class OrderDeleteView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        client = request.user.client
        order_id = request.GET.get("id", None)
        if order_id:
            queryset = Order.objects.filter(id=order_id, client=client)
            queryset.delete()
        response = {"data": []}
        return Response(response)


class OrderItemView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        order = Order.objects.filter(
            id=request.GET.get("order_id", None)
        ).first()

        if order:
            queryset = ItemOrder.objects.filter(order=order)
        else:
            client = request.user.client
            queryset = ItemOrder.objects.filter(
                order__in=Order.objects.filter(client=client)
            )

        serializer = SimpleItemOrderSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class OrderItemDeleteView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        item = get_object_or_404(ItemOrder, id=request.GET.get("id", None))
        order = item.order
        if item:
            item.delete()
        queryset = Order.objects.filter(order=order)
        serializer = ItemOrderSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)
