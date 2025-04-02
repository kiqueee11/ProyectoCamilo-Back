from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from attendances.models import Attendance
from attendances.serializers.create_attendance_serializer import CreateAttendanceSerializer
from attendances.serializers.update_attendance_serializer import UpdateAttendanceSerializer
from events.models import Event
from users.models import CustomUser


class CreateUpdateAttendanceView(APIView):
    def post(self, request):
        data = request.data
        update = data.get('update')
        print(data)

        #Crear attendances si no hay ID

        if not update or update is None:
            if not CustomUser.objects.filter(email=data['user']).exists():
                return Response(
                    {"error": "User not found with email: " + data['user']},
                    status=HTTP_400_BAD_REQUEST
                )

            if not Event.objects.filter(slug=data['event']).exists():
                return Response(
                    {"error": "Event not found with slug: " + data['event']},
                    status=HTTP_400_BAD_REQUEST
                )
            event = Event.objects.get(slug=data['event'])
            data["event"] = event.id

            user = CustomUser.objects.get(email=data['user'])
            data["user"] = user.id
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

        if not Attendance.objects.filter(user__email=data['user'], event__slug=data['event']).exists():
            return Response(
                {"error": "Attendance not found"},
                status=HTTP_400_BAD_REQUEST
            )

        attendance = Attendance.objects.get(user__email=data['user'], event__slug=data['event'])

        event = Event.objects.get(slug=data['event'])
        data["event"] = event.id
        user = CustomUser.objects.get(email=data['user'])
        data["user"] = user.id
        serializer = UpdateAttendanceSerializer(data=data)
        if serializer.is_valid():
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


