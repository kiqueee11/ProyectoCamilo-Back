
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.response import Response

from events.models import Event
from users.models import CustomUser


class DeleteUserView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, slug):
        try:
            event = Event.objects.get(slug=slug)
        except:
            return Response(
                {"error": "Evento no encontrado"},
                status=HTTP_400_BAD_REQUEST
            )

        data = request.data
        user_email = data.get("email")

        try:
            user = CustomUser.objects.get(email=user_email)
            if user not in event.users.all():
                return Response(
                    {"error": "El usuario no está en el evento"},
                    status=HTTP_400_BAD_REQUEST
                )
            else:
                event.users.remove(user)
                return Response(
                    {"success": "Usuario eliminado del evento"},
                    status=HTTP_200_OK
                )
        except:
            return Response(
                {"error": "Usuario no encontrado"},
                status=HTTP_400_BAD_REQUEST
            )

