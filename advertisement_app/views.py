from rest_framework import (
    permissions
)
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

    def get(self, request):
        queryset = Advertisement.objects.all()
        serializer = AdvertisementSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)
