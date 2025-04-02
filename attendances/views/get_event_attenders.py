from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from attendances.models import Attendance
from attendances.serializers import CreateAttendanceSerializer
from events.models import Event


class GetEventAttenders(APIView):
    def get(self,request, event_id):
        if not Event.objects.filter(id=event_id).exists():
            return Response({'error':f'Event not found with id: {event_id}'})

        attenders = Attendance.objects.filter(event_id__exact=event_id, attendance=True).all()
        serializer = CreateAttendanceSerializer(attenders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
