from rest_framework import serializers
from events.models import Event
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from datetime import datetime, time
class AddNewEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['slug', 'created_at', 'updated_at']

    def validate(self, data):
        if not data.get('title'):
            raise serializers.ValidationError({"message": "Title is required"})
        if not data.get('location'):
            raise serializers.ValidationError({"message": "Location is required"})
        if not data.get('description'):
            raise serializers.ValidationError({"message": "Description is required"})
        if not data.get('type'):
            raise serializers.ValidationError({"message": "Type is required"})
        
        date_value = data.get('date')
    
        if isinstance(date_value, str):
            try:
                parsed_date = datetime.strptime(date_value, '%Y-%m-%d')
                print(parsed_date)
                date_with_time = datetime.combine(parsed_date.date(), time(hour=9, minute=0))
                print(date_with_time)
                data["date"] = date_with_time
                print(data)
            except:
                raise serializers.ValidationError({"date": "Formato inválido"})
        return data
    


    
class EventDateFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['date']
        read_only_fields = ['slug', 'created_at', 'updated_at']

    def validate(self, data):
        if not data.get('date'):
            raise serializers.ValidationError({"message": "Date is required"})
      
        
        date_value = data.get('date')
    
        if isinstance(date_value, str):
            try:
                parsed_date = datetime.strptime(date_value, '%Y-%m-%d')
                print(parsed_date)
                date_with_time = datetime.combine(parsed_date.date(), time(hour=9, minute=0))
                print(date_with_time)
                data["date"] = date_with_time
                print(data)
            except:
                raise serializers.ValidationError({"date": "Formato inválido"})
        return data