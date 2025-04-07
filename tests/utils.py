import pytest
from src.models.user import User, UserLogin
from src.models.task import Task, TaskStatus

@pytest.fixture
def test_user():
    return User(
        username="testuser",
        email="test@example.com",
        password="testpassword"
    )

@pytest.fixture
def test_user_login():
    return UserLogin(
        username="testuser",
        password="testpassword"
    )

@pytest.fixture
def test_task():
    return Task(
        title="Test Task",
        description="Test Description",
        status=TaskStatus.todo
    )
