
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from events.models import Event
from events.serializers.EventSerializer import AddNewEventSerializer, EventDateFilterSerializer, EventTypeFilterSerializer, EventTypeTitleSerializer

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
        if serializer.is_valid():
            serializer.save()  # Save the data if valid
            return Response({"success": "Evento creado correctamente"}, status=HTTP_201_CREATED)
        else:
            return Response({"error": serializer.errors}, status=HTTP_400_BAD_REQUEST)
        

class FindEventByDateView(APIView):
    def post(self, request):
        data = request.data
        date = data.get('date')
        serializer = EventDateFilterSerializer(data=data)
       
        if serializer.is_valid():
            date = serializer.validated_data['date']
            events = Event.objects.filter(date__date=date)
            event_serializer = AddNewEventSerializer(events, many=True)
            return Response({"success": "Events found", "events": event_serializer.data}, status=HTTP_200_OK)
        else:
            return Response({"error": serializer.errors}, status=HTTP_400_BAD_REQUEST)


class FindEventByTypeView(APIView):
    def post(self,request):
        data = request.data
        type = data.get('type')
        serializer = EventTypeFilterSerializer(data=data)
        if serializer.is_valid():
            event = Event.objects.filter(type=type)
            return Response({"success": "Events found", "events": event.values()}, status=HTTP_200_OK)
        else:
            return Response({"error": serializer.errors}, status=HTTP_400_BAD_REQUEST)

class FindEventByTitleView(APIView):
    def post(self,request):
        data = request.data
        title = data.get('title')
        serializer = EventTypeTitleSerializer(data=data)
        if serializer.is_valid():
            event = Event.objects.filter(title=title)
            return Response({"success": "Events found", "events": event.values()}, status=HTTP_200_OK)
        else:
            return Response({"error": serializer.errors}, status=HTTP_400_BAD_REQUEST)
        