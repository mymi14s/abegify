import pytest
from user_management.models import CustomUser
from user_management.api.v1.serializers import UserSerializer

@pytest.fixture
def user(db):  # Use the `db` fixture here instead of @pytest.mark.django_db
    """Create a test user in the database."""
    return CustomUser.objects.create_user(
        email="jane@example.com",
        first_name="Jane",
        last_name="Doe",
        password="password123"
    )

def test_serializer_fields(user):
    """Test that the UserSerializer returns the correct fields and values."""
    serializer = UserSerializer(user)
    data = serializer.data

    assert set(data.keys()) == {"email", "first_name", "last_name"}
    assert data['email'] == "jane@example.com"
    assert data['first_name'] == "Jane"
    assert data['last_name'] == "Doe"
