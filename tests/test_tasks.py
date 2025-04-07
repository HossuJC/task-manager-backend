import pytest
from tests.utils import test_user, test_task

@pytest.mark.asyncio
async def test_create_task(test_app, test_user, test_task):
    test_app.post("/register", json=test_user.model_dump())
    login_response = test_app.post("/login", json={"username": "testuser", "password": "testpassword"})
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    response = test_app.post("/tasks", json=test_task.model_dump(), headers=headers)
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["message"] == "Task created"

@pytest.mark.asyncio
async def test_get_tasks(test_app, test_user, test_task):
    test_app.post("/register", json=test_user.model_dump())
    login_response = test_app.post("/login", json={"username": "testuser", "password": "testpassword"})
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    test_app.post("/tasks", json=test_task.model_dump(), headers=headers)
    response = test_app.get("/tasks", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Test Task"

@pytest.mark.asyncio
async def test_update_task(test_app, test_user, test_task):
    test_app.post("/register", json=test_user.model_dump())
    login_response = test_app.post("/login", json={"username": "testuser", "password": "testpassword"})
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    create_response = test_app.post("/tasks", json=test_task.model_dump(), headers=headers)
    task_id = create_response.json()["id"]
    
    updated_task = {"title": "Updated Task", "description": "Updated Description", "status": "in_progress"}
    response = test_app.put(f"/tasks/{task_id}", json=updated_task, headers=headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Task updated"
    
    get_response = test_app.get("/tasks", headers=headers)
    assert get_response.json()[0]["title"] == "Updated Task"
    assert get_response.json()[0]["status"] == "in_progress"

@pytest.mark.asyncio
async def test_delete_task(test_app, test_user, test_task):
    test_app.post("/register", json=test_user.model_dump())
    login_response = test_app.post("/login", json={"username": "testuser", "password": "testpassword"})
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    create_response = test_app.post("/tasks", json=test_task.model_dump(), headers=headers)
    task_id = create_response.json()["id"]
    
    response = test_app.delete(f"/tasks/{task_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted"
    
    get_response = test_app.get("/tasks", headers=headers)
    assert len(get_response.json()) == 0

@pytest.mark.asyncio
async def test_unauthorized_access(test_app, test_task):
    response = test_app.post("/tasks", json=test_task.model_dump())
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"