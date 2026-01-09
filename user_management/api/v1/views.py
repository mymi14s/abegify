from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from user_management.models import CustomUser
from .serializers import UserSerializer

class UserInfoView(APIView):
    """
    API endpoint to get information about the currently logged-in user.
    Requires authentication.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Returns the serialized data of the authenticated user.
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class RequestOTPView(APIView):
    def post(self, request):
        serializer = RequestOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "OTP sent"},
            status=status.HTTP_200_OK
        )


class VerifyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {"message": "Signup successful"},
            status=status.HTTP_201_CREATED
        )


class LinkEmailView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LinkEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(request.user)
        return Response({"message": "Email linked"})
