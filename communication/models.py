from django.db import models
from django.utils.timezone import now


# Create your models here.
class Waitlist(models.Model):
    """
    List for pre launch.
    """
    email = models.EmailField(unique=True, max_length=100)
    created_at = models.DateTimeField(default=now)


    def __str__(self):
        return self.email



class EmailTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subject = models.CharField(max_length=255, help_text="Email subject line (can include placeholders)")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Email Template"
        verbose_name_plural = "Email Templates"

    def __str__(self):
        return f"{self.name}"
        

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"