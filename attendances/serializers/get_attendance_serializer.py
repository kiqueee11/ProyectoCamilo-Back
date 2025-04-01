from rest_framework import serializers

from attendances.models import Attendance
from users.models import CustomUser


class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "name",)

class GetAttendanceSerializer(serializers.ModelSerializer):
    user = NestedUserSerializer()
    class Meta:
        model = Attendance
        fields = ("id","attendance", "user", "event")
        read_only_fields = ('created_at', 'updated_at')