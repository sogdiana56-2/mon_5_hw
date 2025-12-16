from django.core.mail import send_mail
from django.shortcuts import render
from . import models, serializers
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializers, ConfirmSerializer,LoginSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializers
    queryset = User.objects.all()


class LoginAPIView(APIView):
    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        user = authenticate(**serializer.validated_data)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})

        return Response(
            data={'message': 'Invalid credentials'}
        )


class SMSCodeConfirm(APIView):
    def post(self, request):
        serializer = serializers.SMSCodeSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=400)

        sms_code = serializer.validated_data.get('sms_code')

        try:
            sms_code = models.SMSCode.objects.get(code=sms_code)
        except models.SMSCode.DoesNotExist:
            return Response(

                data={'message': 'Code not found'}
            )

        sms_code.user.is_active = True
        sms_code.user.save()
        sms_code.delete()

        return Response( {
  "message": "Account confirmed"
})


