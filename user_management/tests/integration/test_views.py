import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from user_management.models import CustomUser

@pytest.mark.django_db
def test_unauthenticated_access():
    client = APIClient()
    url = reverse('user_management:user-info')
    response = client.get(url)
    assert response.status_code in (401, 403)

@pytest.mark.django_db
def test_authenticated_access():
    user = CustomUser.objects.create_user(
        email="apiuser@example.com",
        first_name="API",
        last_name="User",
        password="apipassword123"
    )
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('user_management:user-info')
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['email'] == user.email
