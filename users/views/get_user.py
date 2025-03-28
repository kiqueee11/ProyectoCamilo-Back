from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from users.models import CustomUser
from users.serializers.UserSerializer import GetUserSerializer


class GetUsersView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        try:
            user = CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "Usuario no encontrado"},
                status=HTTP_400_BAD_REQUEST
            )

        serializer = GetUserSerializer(user)
        return Response(serializer.data, status=HTTP_200_OK)
