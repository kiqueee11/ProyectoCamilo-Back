from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.response import Response
from events.models import Event


class DeleteEventView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, id):
        try:
            events = Event.objects.get(id=id)
            events.delete()
            return Response(
                {"success": "Evento eliminado"},
                status=HTTP_200_OK
            )
        except:
            return Response(
                {"error": "Evento no encontrado"},
                status=HTTP_400_BAD_REQUEST
            )