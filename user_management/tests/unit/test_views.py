
def test_register(client):
    response = client.post("/api/v1/auth/register/", {
        "email": "test@test.com",
        "password": "StrongPass123"
    })
    assert response.status_code == 200
