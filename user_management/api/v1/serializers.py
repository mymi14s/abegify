from django.contrib.auth import authenticate
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from user_management.models import CustomUser, EmailOTP, ReferenceChoice
from user_management.utils import generate_otp


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )
    

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.pop('username', None)
        return data

    def save(self, request):
        """
        Override save to:
        - create user without username
        - optionally deactivate user until OTP verification
        - send OTP to email
        """
        user = super().save(request)

        generate_otp(user, ReferenceChoice.REGISTER)

        return user


class CustomLoginSerializer(LoginSerializer):
    username = None    
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )


class VerifyEmailOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    reference = serializers.ChoiceField(choices=ReferenceChoice.choices)
    password = serializers.CharField(
        write_only=True,
        required=False,
        allow_blank=True,
        style={'input_type': 'password'}
    )

class ResendEmailOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    reference = serializers.ChoiceField(choices=ReferenceChoice.choices)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField()


class ChangeEmailSerializer(serializers.Serializer):
    new_email = serializers.EmailField()


class PhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

