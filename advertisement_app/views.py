from django.http import HttpRequest
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from advertisement_app.models import (
    Advertisement
)
from advertisement_app.serializers import (
    AdvertisementSerializer
)


class AdvertisementView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        queryset = Advertisement.objects.filter(is_active=True)
        serializer = AdvertisementSerializer(queryset, many=True)
        response = {"data": serializer.data,
                    "count": len(queryset),
                    "success": True}
        return Response(response)
