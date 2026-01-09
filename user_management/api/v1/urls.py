
from django.urls import path
from .views import (
    UserInfoView, RequestOTPView, VerifyOTPView, LinkEmailView,
)

app_name = 'user_management'

urlpatterns = [
    path('info/', UserInfoView.as_view(), name='user-info'),
    path('auth/request-otp/', RequestOTPView.as_view()),
    path('auth/verify-otp/', VerifyOTPView.as_view()),
    path('auth/link-email/', LinkEmailView.as_view()),
]
