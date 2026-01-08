from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUseradmin
from django.contrib import admin
from .models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class CustomUserdmin(BaseUseradmin):
    """ Custom user admin display."""

    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Personal Information'), {'fields' :('email', 'first_name', 'last_name')}),
        (_('Additiona Information'), {'fields': ('photo',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important Dates'), {'fields': ('last_login', 'date_joined')}),
        )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2',)
        }),
    )

    ordering = ['email', 'first_name', 'last_name']
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name']
    list_filters = ['email', 'first_name', 'last_name']
    filter_horizontal = ['groups', 'user_permissions']
