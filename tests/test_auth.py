import pytest
from tests.utils import test_user, test_user_login
from src.models.user import User

@pytest.mark.asyncio
async def test_register_user(test_app, test_user):
    response = test_app.post("/register", json=test_user.model_dump())
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["message"] == "User successfully registered"

@pytest.mark.asyncio
async def test_register_duplicate_user(test_app, test_user):
    test_app.post("/register", json=test_user.model_dump())
    response = test_app.post("/register", json=test_user.model_dump())
    assert response.status_code == 400
    assert response.json()["detail"] == "Username or email already exists"

@pytest.mark.asyncio
async def test_login_user(test_app, test_user, test_user_login):
    test_app.post("/register", json=test_user.model_dump())
    response = test_app.post("/login", json=test_user_login.model_dump())
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
    assert "user" in response.json()

@pytest.mark.asyncio
async def test_login_invalid_credentials(test_app, test_user):
    test_app.post("/register", json=test_user.model_dump())
    response = test_app.post("/login", json={"username": "testuser", "password": "wrong"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Wrong credentials"