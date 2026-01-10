
import requests, json
from django.core.mail import send_mail
from django.core.files.base import ContentFile
from allauth.socialaccount.signals import social_account_added, social_account_updated
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added, social_account_updated
from user_management.models import EmailOTP

@receiver(post_save, sender=EmailAddress)
def mark_email_verified_email_address(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        email = user.email

        if not email:
            return

        if instance.verified:
            if not user.email_verified:
                user.email_verified = True
                user.save()


@receiver(post_save, sender=SocialAccount)
def mark_email_verified_on_social_account(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        email = user.email

        if not email:
            return

        if not user.email_verified:
            user.email_verified = True
            user.save()

        instance.extra_data
        avatar_url = instance.extra_data.get("picture") or instance.extra_data.get("avatar_url")

        # Only attempt to save if an avatar URL exists and user doesn't have one yet
        if avatar_url and not user.photo:
            try:
                response = requests.get(avatar_url, timeout=10)
                if response.status_code == 200:
                    file_name = f"social_avatar_{user.id}.png"
                    user.photo.save(
                        file_name,
                        ContentFile(response.content),
                        save=False, # We will save the user model once at the end
                    )
            except Exception as e:
                # Log the error if you have a logger, otherwise fail silently
                print(f"Failed to fetch avatar: {e}")

        user.save()


@receiver(post_save, sender=EmailOTP)
def send_email_otp(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="Your verification code",
            message=f"Your verification code is {instance.otp}. It expires in 10 minutes.",
            from_email=None,
            recipient_list=[instance.email],
        )
