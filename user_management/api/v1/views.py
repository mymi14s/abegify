from django.contrib.auth import login

from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

from .serializers import *

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(is_active=False)
        # send OTP here
        return Response({"detail": "OTP sent to email"})


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login(request, serializer.validated_data)
        return Response({"detail": "Login successful"})


class ForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # send reset email
        return Response({"detail": "Password reset email sent"})


class ChangeEmailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangeEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.email = serializer.validated_data["new_email"]
        request.user.email_verified = False
        request.user.save()
        return Response({"detail": "Email changed, verify again"})


class AddPhoneNumberAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PhoneNumberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.phone_number = serializer.validated_data["phone_number"]
        request.user.save()
        return Response({"detail": "Phone number added"})


class GoogleLoginAPIView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


