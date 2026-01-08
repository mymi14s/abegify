from django.contrib import admin
from .models import Waitlist, EmailTemplate, ContactForm

# Register your models here.
@admin.register(Waitlist)
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    list_filter = ('email',)
    search_fields = ('email',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)


@admin.register(EmailTemplate)
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'is_active', 'updated_at', 'created_at')
    list_filter = ('name',)
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(ContactForm)
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'message', 'updated_at', 'created_at')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)