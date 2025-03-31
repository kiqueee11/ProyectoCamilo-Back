from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from attendances.models import Attendance
from attendances.serializers.create_attendance_serializer import CreateAttendanceSerializer
from attendances.serializers.update_attendance_serializer import UpdateAttendanceSerializer


class CreateUpdateAttendanceView(APIView):
    def post(self, request):
        data = request.data
        attendance_id = data.get('id')
        print(data)

        #Crear attendances si no hay ID

        if not attendance_id:
            serializer = CreateAttendanceSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Attendance created correctly"},
                        status=HTTP_200_OK
                )
            else:
                return Response({"message": serializer.errors},
                                status=HTTP_400_BAD_REQUEST
                )

        # Actualizar attendances

        serializer = UpdateAttendanceSerializer(data=data)
        if serializer.is_valid():
            attendance = Attendance.objects.get(id=attendance_id)
            attendance.attendance = data["attendance"]
            attendance.save()
            return Response(
                {"message": "Attendance updated correctly"},
                status=HTTP_200_OK
            )
        else:
            return Response(
                {"message": serializer.errors},
                status=HTTP_400_BAD_REQUEST
            )


