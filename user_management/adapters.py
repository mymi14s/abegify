from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.http import Http404
from django.conf import settings


class NoSignupAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        # Completely disable signups
        return False

    def respond_user_inactive(self, request, user):
        # Optional: handle inactive users differently
        raise Http404


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        if sociallogin.user.id:
            return

        email = sociallogin.account.extra_data.get("email")
        if not email:
            return

        from user_management.models import CustomUser
        try:
            user = CustomUser.objects.get(email=email)
            sociallogin.connect(request, user)
        except CustomUser.DoesNotExist:
            pass


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        return (
            f"{settings.FRONTEND_URL}/verify-email?"
            f"key={emailconfirmation.key}"
        )

    def send_confirmation_mail(self, request, emailconfirmation, signup):
        pass
