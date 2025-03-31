from rest_framework import serializers

from attendances.models import Attendance
from users.serializers.UserSerializer import AddNewUserSerializer


class GetAttendanceSerializer(serializers.Serializer):
    user = AddNewUserSerializer()

    class Meta:
        model = Attendance
        fields = ("id", "event", "attendance", "user")
