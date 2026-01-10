import random
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from user_management.models import EmailOTP

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

    # send OTP email
    send_mail(
        subject="Your Password Reset OTP",
        message=f"Your OTP for password reset is {otp}. It expires in 10 minutes.",
        from_email=None,  # uses DEFAULT_FROM_EMAIL
        recipient_list=[email],
        fail_silently=False,
    )
    
