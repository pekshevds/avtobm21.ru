from rest_framework import permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from auth_app.models import User
from auth_app.serializers import UserSerializer


class UserView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        username = request.GET.get("username", "")
        if username:
            queryset = User.objects.filter(username=username)
            serializer = UserSerializer(queryset, many=True)
        else:
            queryset = User.objects.filter(is_superuser=False)
            serializer = UserSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)
