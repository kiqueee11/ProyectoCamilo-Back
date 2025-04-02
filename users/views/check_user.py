from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from users.models.user_model import CustomUser
from users.serializers.UserSerializer import GetUserSerializer


class checkUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                
                return Response({"success": "Usuario encontrado"}, status=HTTP_200_OK)
            else:
                return Response({"error": "Contraseña incorrecta"}, status=HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=HTTP_400_BAD_REQUEST)