from rest_framework import serializers
from attendances.models.attendance_model import Attendance
from events.models import Event
from users.models import CustomUser

class CreateAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ("attendance", "user", "event")
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, data):
        attendance = data.get('attendance', True)
        event = data.get('event')
        user = data.get('user')

        if attendance is None or event is None or user is None:
            raise serializers.ValidationError('Mandatory fields are missing (attendance, event, user)')

        if not isinstance(attendance, bool):
            raise serializers.ValidationError(f'Attendance is not a boolean value')

        if Attendance.objects.filter(event=event, user=user).exists():
            raise serializers.ValidationError(f'Attendance already exists')

        return data

