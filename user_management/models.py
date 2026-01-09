from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.db import models


class UserProfileManager(BaseUserManager):
    def create_user(
        self,
        phone_number=None,
        email=None,
        password=None,
        **extra_fields
    ):
        """
        Normal users:
        - phone_number REQUIRED
        - email OPTIONAL
        - password NOT required (OTP based)
        """

        if not phone_number and not email:
            raise ValueError("A phone number or email must be provided")

        if email:
            email = self.normalize_email(email)

        user = self.model(
            phone_number=phone_number,
            email=email,
            **extra_fields
        )

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Admin users:
        - email REQUIRED
        - password REQUIRED
        - phone_number OPTIONAL
        """

        if not email:
            raise ValueError("Superuser must have an email")

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(
            email=email,
            password=password,
            **extra_fields
        )


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True
    )

    email = models.EmailField(
        unique=True,
        null=True,
        blank=True
    )

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    photo = models.ImageField(upload_to='users/photos', blank=True, null=True)

    is_active = models.BooleanField(default=False) 
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email or self.phone_number

    def clean(self):
        if self.is_staff or self.is_superuser:
            if not self.email:
                raise ValidationError("Staff users must have an email")
        else:
            if not self.phone_number:
                raise ValidationError("Normal users must have a phone number")



class PhoneOTP(models.Model):
    phone_number = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created_at + timezone.timedelta(minutes=5)


