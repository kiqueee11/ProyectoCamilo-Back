
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from rest_framework.views import APIView

from users.models import CustomUser
from users.serializers.UserSerializer import AddNewUserSerializer


class AddNewUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, id):
        try:
            user = CustomUser.objects.get(id=id)
        except:
            return Response(
                {"error": "Usuario no encontrado"},
                status=HTTP_400_BAD_REQUEST
            )

        data = request.data
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone", "")
        password = data.get("password")
        is_active = data.get("is_active", True)
        is_staff = data.get("is_staff", False)
        is_superuser = data.get("is_superuser", True)

        data["is_active"] = is_active
        data["is_staff"] = is_staff
        data["is_superuser"] = is_superuser

        serializer = AddNewUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": "Usuario creada correctamente"},
                status=HTTP_201_CREATED
            )
        else:
            return Response(
                {"error": serializer.errors},
                status=HTTP_400_BAD_REQUEST
            )