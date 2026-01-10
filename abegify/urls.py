"""
URL configuration for abegify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from dj_rest_auth.views import LoginView, LogoutView, PasswordChangeView
from dj_rest_auth.registration.views import RegisterView, SocialLoginView

from .views import home, privacy, terms

admin.site.site_header = "Abegify Portal Admin"
admin.site.site_title = "Abegify Admin"
admin.site.index_title = "Welcome to Abegify Administration"



urlpatterns = [
    path('', home, name='home'),
    path('privacy-policy', privacy, name='privacy-policy'),
    path('terms-and-conditions', terms, name='terms-and-conditions'),
    path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')), 

    # dj-rest-auth URLs
    path("api/auth/login/", LoginView.as_view(), name="rest_login"),
    path("api/auth/logout/", LogoutView.as_view(), name="rest_logout"),
    path("api/auth/password/change/", PasswordChangeView.as_view(), name="rest_password_change"),
    path("api/auth/registration/", RegisterView.as_view(), name="rest_register"),
    path("api/auth/google/", SocialLoginView.as_view(), name="google_login"),

    path('api/v1/user/', include('user_management.api.v1.urls')),
    path('api/v1/communication/', include('communication.api.v1.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    # ReDoc UI
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema')),
]


# Display images
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)