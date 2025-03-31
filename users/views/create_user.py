
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR

from rest_framework.views import APIView

from users.models import CustomUser
from users.serializers.UserSerializer import AddNewUserSerializer


class CreateNewUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not email or not name or not password:
            return Response(
                {"error": "Faltan campos obligatorios"},
                status=HTTP_400_BAD_REQUEST
            )
        if CustomUser.objects.filter(email=email).exists():
            return Response(
                {"error": "No se pueden crear más contactos con ese correo"},
                status=HTTP_400_BAD_REQUEST
            )

        try:
            phone = data.get("phone", "")
            is_active = data.get("is_active", True)
            is_staff = data.get("is_staff", False)
            is_superuser = data.get("is_superuser", False)
            data["is_active"] = is_active
            data["is_staff"] = is_staff
            data["is_superuser"] = is_superuser
            serializer = AddNewUserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"success": "Usuario creado correctamente"},
                    status=HTTP_201_CREATED
                )
            else:
                return Response(
                    {"error": serializer.errors},
                    status=HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"error": f'error{e}'},
                status=HTTP_500_INTERNAL_SERVER_ERROR
            )


