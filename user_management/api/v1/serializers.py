import random
from rest_framework import serializers
from user_management.models import CustomUser, PhoneOTP

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
        read_only_fields = fields 


class RequestOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

    def create(self, validated_data):
        otp = str(random.randint(100000, 999999))

        PhoneOTP.objects.create(
            phone_number=validated_data['phone_number'],
            otp=otp
        )

        # 🔔 send OTP via SMS provider here

        return validated_data



class VerifyOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    otp = serializers.CharField()

    def validate(self, attrs):
        try:
            record = PhoneOTP.objects.filter(
                phone_number=attrs['phone_number']
            ).latest('created_at')
        except PhoneOTP.DoesNotExist:
            raise serializers.ValidationError("OTP not found")

        if record.otp != attrs['otp']:
            raise serializers.ValidationError("Invalid OTP")

        if record.is_expired():
            raise serializers.ValidationError("OTP expired")

        return attrs

    def create(self, validated_data):
        user, _ = CustomUser.objects.get_or_create(
            phone_number=validated_data['phone_number']
        )
        user.is_active = True
        user.save()
        return user


class LinkEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use")
        return value

    def save(self, user):
        user.email = self.validated_data['email']
        user.save()
        return user
