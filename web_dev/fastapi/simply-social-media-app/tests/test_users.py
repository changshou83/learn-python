import pytest
import jwt

from app.core.config import get_settings
from app.schemas import Token, UserRead


def test_create_user(client):
    response = client.post(
        "/users/",
        json={"email": "hello123@gmail.com", "password": "password123"},
    )

    user = UserRead(**response.json())
    assert user.email == "hello123@gmail.com"
    assert response.status_code == 201


def test_login_user(test_user, client):
    response = client.post(
        "/login",
        data={"username": test_user["email"], "password": test_user["password"]},
    )

    login_response = Token(**response.json())
    settings = get_settings()
    payload = jwt.decode(
        login_response.access_token,
        settings.secret_key,
        algorithms=[settings.algorithm],
    )
    assert payload.get("user_id") == test_user["id"]
    assert login_response.token_type == "bearer"
    assert response.status_code == 200


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("wrongemail@gmail.com", "password123", 403),
        ("sanjeev@gmail.com", "wrongpassword", 403),
        ("wrongemail@gmail.com", "wrongpassword", 403),
        (None, "password123", 422),
        ("sanjeev@gmail.com", None, 422),
    ],
)
def test_incorrect_login(test_user, client, email, password, status_code):
    response = client.post(
        "/login",
        data={"username": email, "password": password},
    )
    assert response.status_code == status_code

