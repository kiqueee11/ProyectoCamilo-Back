from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from attendances.models.attendance_model import Attendance
from attendances.serializers import CreateAttendanceSerializer
from attendances.serializers.get_attendance_serializer import GetAttendanceSerializer
from events.models import Event


class GetAttendancesByEventIdView(APIView):
    def get(self, request, event_id):
        if not Event.objects.filter(id=event_id).exists():
            return Response(
                {"error": f"Event not found with id: {event_id}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        attendances = Attendance.objects.filter(event_id__exact=event_id).all()
        attendances_serializer = CreateAttendanceSerializer(attendances, many=True)
        return Response(attendances_serializer.data, status=status.HTTP_200_OK)