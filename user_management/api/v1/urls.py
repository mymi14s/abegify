
from django.urls import path
from .views import UserInfoView

app_name = 'user_management'

urlpatterns = [
    path('info/', UserInfoView.as_view(), name='user-info'),
]
