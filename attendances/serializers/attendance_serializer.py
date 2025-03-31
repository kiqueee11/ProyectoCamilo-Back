from rest_framework import serializers
from attendances.models.attendance_model import Attendance
from users.models import CustomUser


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, data):
        attendance = data['attendances']
        event_id = data['event']
        user_id = data['user']

        if not attendance or not event_id or not user_id:
            raise serializers.ValidationError('Mandatory fields are missing (attendances, event, user)')

        if not event_id:
            raise serializers.ValidationError(f'Event not found with id: {event_id}')

        if not CustomUser.objects.filter(id=user_id).exists():
            raise serializers.ValidationError(f'User not found with id: {user_id}')

        if not isinstance(attendance, bool):
            raise serializers.ValidationError(f'Attendance is not a boolean value')

        return data

