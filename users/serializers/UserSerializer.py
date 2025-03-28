from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import CustomUser

class AddNewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password':{"write_only": True}
        }

    @staticmethod
    def validate_email(value):
        if value.endswith(".ru"):
            raise serializers.ValidationError("No se permiten dominios .ru")
        return value

    @staticmethod
    def validate_phone(value):
        if value and not value.isdigit():
            raise serializers.ValidationError("El teléfono solo debe contener números")
        return value

    @staticmethod
    def validate_password(value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value

    @staticmethod
    def validate_values(self, data):
        if "name" not in data or not data("name"):
            raise serializers.ValidationError({"name": "El nombre es obligatorio"})
        if "email" not in data or not data("email"):
            raise serializers.ValidationError({"email": "El correo es obligatorio"})
        if "password" not in data or not data ("password"):
            raise serializers.ValidationError({"password": "La contraseña es obligatoria"})
        return data

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password':{"write_only": True}
        }