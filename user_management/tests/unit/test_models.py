import pytest
from user_management.models import CustomUser

@pytest.mark.django_db
def test_user_creation():
    user = CustomUser.objects.create_user(
        email="test@example.com",
        first_name="John",
        last_name="Doe",
        password="password123"
    )
    assert user.email == "test@example.com"
    assert user.check_password("password123")
    assert not user.is_staff

@pytest.mark.django_db
def test_superuser_creation():
    admin = CustomUser.objects.create_superuser(
        email="admin@example.com",
        first_name="Admin",
        last_name="User",
        password="adminpass"
    )
    assert admin.is_superuser
    assert admin.is_staff
