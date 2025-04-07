from fastapi import APIRouter, HTTPException, Depends
from src.models.task import Task
from src.auth.middleware import get_current_user
from src.services.task_service import create_task, get_tasks, update_task, delete_task

router = APIRouter()

@router.post("/tasks", dependencies=[Depends(get_current_user)])
async def add_task(task: Task):
    """
    Creates a new task.
    
    **Parameters:**
    - **task (Task):** Object containing task data.
    
    **Returns:**
    - **dict:** ID of the created task and confirmation message.
    """
    task_id = await create_task(task)
    return {"id": task_id, "message": "Task created"}

@router.get("/tasks", dependencies=[Depends(get_current_user)])
async def list_tasks():
    """
    Retrieves all registered tasks.
    
    **Returns:**
    - **list:** List of tasks.
    """
    return await get_tasks()

@router.put("/tasks/{task_id}", dependencies=[Depends(get_current_user)])
async def change_task_status(task_id: str, task: Task):
    """
    Updates a specific task by ID.
    
    **Parameters:**
    - **task_id (str):** ID of the task to update.
    - **task (Task):** Updated task data.
    
    **Returns:**
    - **dict:** Confirmation message if the update was successful.
    - **HTTPException:** 404 error if the task was not found.
    """
    if await update_task(task_id, task):
        return {"message": "Task updated"}
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{task_id}", dependencies=[Depends(get_current_user)])
async def remove_task(task_id: str):
    """
    Deletes a task by its ID.
    
    **Parameters:**
    - **task_id (str):** ID of the task to delete.
    
    **Returns:**
    - **dict:** Confirmation message if the deletion was successful.
    - **HTTPException:** 404 error if the task was not found.
    """
    if await delete_task(task_id):
        return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
