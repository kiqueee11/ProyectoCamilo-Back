from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from attendances.models import Attendance
from attendances.serializers.attendance_serializer import AttendanceSerializer


class CreateUpdateAttendanceView(APIView):
    def post(self, request):
        data = request.data

        #Crear attendances si no hay ID

        if not data["id"]:
            serializer = AttendanceSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Attendance created correctly"},
                        status=HTTP_200_OK
                )

        # Actualizar attendances

        attendance = Attendance.objects.get(id=data["id"])
        attendance.attendance = data["attendances"]
        serializer = AttendanceSerializer(data=attendance)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Attendance created correctly"},
                status=HTTP_200_OK
            )


