from typing import Any
from django.http import HttpRequest
from rest_framework import permissions, authentication, status
from rest_framework.views import APIView
from rest_framework.response import Response
from kamaz_tech_app.serializers import BodySerializer
from kamaz_tech_app.utils import get_auth_token, load_services


class LoadServicesView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request: HttpRequest) -> Response:
        serialiser = BodySerializer(data=request.data)
        if not serialiser.is_valid():
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serialiser.validated_data
        auth = validated_data.get("auth")
        data = validated_data.get("data")
        token = get_auth_token(auth.get("username"), auth.get("password"))
        if token:
            load_services(token, data)
        response: dict[str, Any] = {}
        return Response(response)
