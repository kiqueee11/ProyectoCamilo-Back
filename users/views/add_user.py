from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from events.models import Event
from users.models import CustomUser


class AddUserToEventView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, slug):
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

            if event.users.filter(id=user.id).exists():
                return Response(
                    {"message": "El usuario ya está en el evento"},
                    status=HTTP_400_BAD_REQUEST
                )
            else:
                event.users.add(user)
                return Response(
                    {"success": "Usuario añadido al evento"},
                    status=HTTP_200_OK
                )
        except:
            return Response(
                {"error": "Usuario no existe"},
                status=HTTP_400_BAD_REQUEST
            )