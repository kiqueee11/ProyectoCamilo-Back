
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED

from events.serializers.EventSerializer import AddNewEventSerializer

class CreateEventView(APIView):
    def post(self, request):

        data = request.data
        title = data.get('title')
        description = data.get('description')
        date = data.get('date')
        location = data.get('location')
        type = data.get('type')
        stars = data.get('stars')

        serializer = AddNewEventSerializer(data=data)
            # Validate the serializer
        if serializer.is_valid():
            serializer.save()  # Save the data if valid
            return Response({"success": "Evento creado correctamente"}, status=HTTP_201_CREATED)
        else:
            # Return validation errors
            return Response({"error": serializer.errors}, status=HTTP_400_BAD_REQUEST)
       