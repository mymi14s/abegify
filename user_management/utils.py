import random
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from user_management.models import EmailOTP

def generate_otp():
    return f"{random.randint(100000, 999999)}"

def create_email_otp(user):
    otp = generate_otp()

    EmailOTP.objects.update_or_create(
        email=user.email,
        defaults={
            "otp": otp,
            "expires_at": timezone.now() + timedelta(minutes=10),
        },
    )


