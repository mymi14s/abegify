
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from .models import CustomUser, EmailOTP, PasswordResetRequest
# Register your models here.


from .models import CustomUser, EmailOTP, PasswordResetRequest
admin.site.register(PasswordResetRequest)

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    ordering = ("email",)
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "email_verified",
        "date_joined",
    )
    list_filter = (
        "is_active",
        "is_staff",
        "is_superuser",
        "email_verified",
        "date_joined",
    )
    search_fields = ("email", "first_name", "last_name")
    readonly_fields = ("date_joined", "last_login")

    fieldsets = (
        (_("Authentication"), {
            "fields": ("email", "password")
        }),
        (_("Personal info"), {
            "fields": (
                "first_name",
                "last_name",
                "phone_number",
                "photo",
            )
        }),
        (_("Permissions"), {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        (_("Verification"), {
            "fields": ("email_verified",)
        }),
        (_("Important dates"), {
            "fields": ("last_login", "date_joined")
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
                "is_staff",
                "is_superuser",
            ),
        }),
    )

    filter_horizontal = ("groups", "user_permissions")

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ("password",)
        return self.readonly_fields

    # def has_delete_permission(self, request, obj=None):
    #     if obj and obj.socialaccount_set.exists():
    #         return False
    #     return super().has_delete_permission(request, obj)




@admin.register(EmailOTP)
class EmailOTPAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "otp",
        "is_used",
        "created_at",
    )
    list_filter = ("is_used", "created_at")
    search_fields = ("email",)
    readonly_fields = ("created_at",)

    actions = ["mark_as_used"]

    @admin.action(description="Mark selected OTPs as used")
    def mark_as_used(self, request, queryset):
        queryset.update(is_used=True)
