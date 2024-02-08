from rest_framework import serializers
from .models import User
from rest_framework.validators import ValidationError


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    birthdate = serializers.DateField(allow_null=True, required=False)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    is_employee = serializers.BooleanField(default=False)
    password = serializers.CharField(max_length=128, write_only=True)
    is_superuser = serializers.BooleanField(default=False, read_only=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("email already registered.")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise ValidationError("username already taken.")
        return value

    def create(self, validated_data):
        if validated_data["is_employee"] is False:
            new_user = User.objects.create_user(**validated_data)
        else:
            new_user = User.objects.create_superuser(**validated_data)
        return new_user

    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance
