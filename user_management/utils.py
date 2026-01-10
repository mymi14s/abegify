import random
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from user_management.models import EmailOTP, ReferenceChoice

def generate_otp():
    return f"{random.randint(100000, 999999)}"



def generate_otp(email, reference):
    otp = f"{random.randint(100000, 999999)}"
    expires_at = timezone.now() + timezone.timedelta(minutes=10)

    EmailOTP.objects.create(
        email=email,
        otp=otp,
        reference=reference,
        expires_at=expires_at
    )

    
