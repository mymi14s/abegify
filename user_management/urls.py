from django.urls import path
from .views import user_login, sio_sid, logout_view, login_view

app_name = 'user_management'

urlpatterns = [
    path('login', user_login, name='login'),
    path('sio-sid', sio_sid, name='sio_sid'),
    path('logout', logout_view, name='logout'),
    path("login1", login_view, name="login"),
]