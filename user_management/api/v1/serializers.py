from rest_framework import serializers
from user_management.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
        read_only_fields = fields 
