from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication
from client_app.serializers import ClientSerializer


class ClientView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        client = request.user.client
        serializer = ClientSerializer(client)
        response = {"data": serializer.data}
        return Response(response)
