from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from attendances.models import Attendance


class GetEventAttendanceStadisticsView(APIView):
    def get(self, request, event_id):
        if not event_id:
            return Response(
                {"error": f"Event not found with id: {event_id}"},
                status=HTTP_400_BAD_REQUEST)

        attendance = Attendance.objects.filter(event_id__exact=event_id).all()
        attenders = Attendance.objects.filter(event_id__exact=event_id, attendance=True).all()

        return Response(
            {"registered": len(attendance), "attenders": len(attenders)},
            status=HTTP_200_OK
        )

