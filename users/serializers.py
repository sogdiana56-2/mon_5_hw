from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class RegisterSerializers(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=6)
    comfirm_password = serializers.CharField(max_length=6)

    def validate(self, data):
        if data ['password'] != data ['comfirm_password']:
            raise serializers.ValidationError('Passwords do not match')
        return data

    def validate_username(self, username):
        try:
            User.objects.filter(username=username).exists()
        except User.DoesNotExixt:
            return username
        raise serializers.ValidationError('this username is already taken')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=6)
    password = serializers.CharField(max_length=6)


class SMSCodeSerializer(serializers.Serializer):
    sms_code = serializers.CharField(max_length=6)

