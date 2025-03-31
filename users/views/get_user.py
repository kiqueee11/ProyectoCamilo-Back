from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from events.models import Event
from users.models import CustomUser
from users.serializers.UserSerializer import GetUserSerializer


class GetUsersView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, slug):
        try:
            event = Event.objects.get(slug=slug)
        except:
            return Response(
                {"error": "Evento no encontrado"},
                status=HTTP_400_BAD_REQUEST
            )


        users_list = [{
            "name": users.name,
            "email": users.email,
        } for users in event.users.all()
        ]
        return Response({"users": users_list}, status=HTTP_200_OK)


