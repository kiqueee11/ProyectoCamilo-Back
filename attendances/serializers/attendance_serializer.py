from rest_framework import serializers
from attendances.models.attendance_model import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, data):
        attendance = data['attendances']
        event = data['event_id']
        user = data['user_id']

        if not attendance or not event or not user:
            raise serializers.ValidationError('Mandatory fields are missing (attendances, event, user)')

        if not event:
            raise serializers.ValidationError(f'Event not found with id: {event}')

        if not user:
            raise serializers.ValidationError(f'User not found with id: {user}')

        if not isinstance(attendance, bool):
            raise serializers.ValidationError(f'Attendance is not a boolean value')

        return data

