from django.urls import path

from .views import *

urlpatterns = [
    path("auth/forgot-password/", ResetPasswordOTPAPIView.as_view(), name="forgot-password"),
    path("auth/set-password/", ResetPasswordAPIView.as_view(), name="set-password"),
    path("auth/change-email/", ChangeEmailAPIView.as_view(), name="change-email"),
    path("auth/add-phone/", AddPhoneNumberAPIView.as_view(), name="add-phone"),
    path("auth/google/", GoogleLoginAPIView.as_view(), name="google-api-login"),
    path("auth/verify-email-otp/", VerifyEmailOTPAPIView.as_view(), name="verify-email-otp"),
    path("auth/resend-email-otp/", ResendEmailOTPAPIView.as_view(), name="resend-email-otp"),
]
