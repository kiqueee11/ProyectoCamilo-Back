from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from attendances.models import Attendance
from attendances.serializers import CreateAttendanceSerializer
from attendances.serializers.get_attendance_serializer import GetAttendanceSerializer
from events.models import Event


class GetEventAttenders(APIView):
    def get(self,request, slug):
        if not Event.objects.filter(slug=slug).exists():
            return Response({'error':f'Event not found with slug: {slug}'})

        attenders = Attendance.objects.filter(event__slug=slug, attendance=True).all()
        serializer = GetAttendanceSerializer(attenders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
