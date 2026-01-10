from django.urls import path
from .views import *

urlpatterns = [
    path("auth/register/", RegisterAPIView.as_view()),
    path("auth/login/", LoginAPIView.as_view()),
    path("auth/forgot-password/", ForgotPasswordAPIView.as_view()),
    path("auth/change-email/", ChangeEmailAPIView.as_view()),
    path("auth/add-phone/", AddPhoneNumberAPIView.as_view()),
    path("auth/google/", GoogleLoginAPIView.as_view(), name="google-api-login"),
    path("auth/verify-email-otp/", VerifyEmailOTPAPIView.as_view()),
    path("auth/resend-email-otp/", ResendEmailOTPAPIView.as_view()),
]
