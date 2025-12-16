from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SMSCode
import random


class RegisterSerializers(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=6)
    comfirm_password = serializers.CharField(max_length=6)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "comfirm_password"]

        def create(self, validated_data):
            password = validated_data.pop("password")
            user = User.objects.create(
                username=validated_data["username"],
                email=validated_data.get("email", ""),
                is_active=False
            )
            user.set_password(password)
            user.save()

            code = str(random.randint(100000, 999999))
            ConfirmCode.objects.create(user=user, code=code)

            user.confirmation_code = code
            return user

class ConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=6)
    password = serializers.CharField(max_length=6)


class SMSCodeSerializer(serializers.Serializer):
    sms_code = serializers.CharField(max_length=6)

