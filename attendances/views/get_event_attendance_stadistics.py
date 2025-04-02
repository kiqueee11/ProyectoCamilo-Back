from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from attendances.models import Attendance
from events.models import Event


class GetEventAttendanceStadisticsView(APIView):
    def get(self, request, slug):
        if not Event.objects.filter(slug=slug).exists():
            return Response(
                {"error": f"Event not found with slug: {slug}"},
                status=HTTP_400_BAD_REQUEST)

        attendance = Attendance.objects.filter(event__slug=slug).all()
        attenders = Attendance.objects.filter(event__slug=slug, attendance=True).all()

        return Response(
            {"registered": len(attendance), "attenders": len(attenders),
             "missing": len(attendance) - len(attenders)},
            status=HTTP_200_OK
        )

