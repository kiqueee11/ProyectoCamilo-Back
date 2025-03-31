from rest_framework import serializers
from attendances.models.attendance_model import Attendance
from events.models import Event
from users.models import CustomUser


class UpdateAttendanceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Attendance
        fields = ("id", "attendance")
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, data):
        attendance_id = data.get("id", None)
        attendance = data.get("attendance", None)

        if attendance is None or attendance_id is None:
            raise serializers.ValidationError('Mandatory fields are missing (id, attendance)')

        if not Attendance.objects.filter(id=attendance_id).exists():
            raise serializers.ValidationError(f'Attendance not found with id: {attendance_id}')

        if not isinstance(attendance, bool):
            raise serializers.ValidationError(f'Attendance is not a boolean value')

        return data

