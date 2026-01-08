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