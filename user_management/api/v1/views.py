from django.contrib.auth import login

from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_spectacular.utils import extend_schema

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress

from user_management.utils import generate_otp
from user_management.models import ReferenceChoice


from .serializers import *

User = get_user_model()


class VerifyEmailOTPAPIView(APIView):
    """
    Verify Email OTP
    """
    permission_classes = [AllowAny]
    serializer_class = VerifyEmailOTPSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not User.objects.filter(email=serializer.validated_data["email"]).exists():
                return Response({"detail": "User does not exists"}, status=400)
            
        if not EmailOTP.objects.filter(
                email=serializer.validated_data["email"], 
                reference=serializer.validated_data["reference"],
                is_used=1
            ).exists():
            return Response({"detail": "Invalid OTP Verification"}, status=400)
            
        user = User.objects.get(email=serializer.validated_data["email"])
        record = EmailOTP.objects.get(
            email=user.email, 
            reference=serializer.validated_data["reference"],
            is_used=1
        )
        if not record.is_valid():
                return Response({"detail": "OTP expired"}, status=400)

        if record.otp != serializer.validated_data["otp"]:
            return Response({"detail": "Invalid OTP"}, status=400)
        
        if serializer.validated_data["reference"] == ReferenceChoice.REGISTER:

            email_address = EmailAddress.objects.get(user=user, email=user.email)
            email_address.verified = True
            email_address.save()

            record.is_used = 1
            record.save()
            user.email_verified = True
            user.save()

            return Response({"detail": "Email verified successfully"})

        elif serializer.validated_data["reference"] == ReferenceChoice.RESET_PASSWORD:
            user.set_password(serializer.validated_data["password"])
            user.save()
            record.is_used = 1
            record.save()
            return Response({"detail": "Password reset successfully"})


class ResendEmailOTPAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ResendEmailOTPSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(email=serializer.validated_data["email"])
        generate_otp(user, serializer.validated_data["reference"])
        return Response({"detail": "OTP resent"})


class ForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        # send reset email
        return Response({"detail": "Password reset email sent"})

class ForgotPassworOTPAPIView(APIView):
    """
    Replaces dj-rest-auth /password/reset/ endpoint
    Sends a 6-digit OTP to email instead of a reset link
    """
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        serializer = PasswordResetOTPRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]

        if not User.objects.filter(email=email).exists():
            return Response({"detail": "User with this email does not exist."}, status=400)

        generate_otp(email, reference=ReferenceChoice.RESET_PASSWORD)
        return Response({"detail": "OTP sent to email."}, status=200)



class ChangeEmailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=ChangeEmailSerializer,
        responses={200: {"detail": "Email changed, verify again"}},
        description="Change authenticated user's email"
    )

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


@extend_schema(
    description="Login with Google OAuth2"
)
class GoogleLoginAPIView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


