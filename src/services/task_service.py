from src.config import db
from src.models.task import Task
from bson import ObjectId

async def create_task(task: Task):
    """
    Creates a new task in the database.
    
    **Parameters:**
    - **task (Task):** Object with task data.
    
    **Returns:**
    - **str:** ID of the created task.
    """
    task_dict = task.model_dump()
    result = await db.tasks.insert_one(task_dict)
    return str(result.inserted_id)

async def get_tasks():
    """
    Retrieves all tasks from the database.
    
    **Returns:**
    - **list:** List of tasks with their data.
    """
    return [dict(task, _id=str(task["_id"])) async for task in db.tasks.find()]

async def update_task(task_id: str, task: Task):
    """
    Updates an existing task in the database.
    
    **Parameters:**
    - **task_id (str):** ID of the task to update.
    - **task (Task):** Updated task data.
    
    **Returns:**
    - **bool:** `True` if the update was successful, `False` otherwise.
    """
    result = await db.tasks.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"title": task.title, "description": task.description, "status": task.status}}
    )
    return result.modified_count > 0

async def delete_task(task_id: str):
    """
    Deletes a task from the database by its ID.
    
    **Parameters:**
    - **task_id (str):** ID of the task to delete.
    
    **Returns:**
    - **bool:** `True` if deletion was successful, `False` otherwise.
    """
    result = await db.tasks.delete_one({"_id": ObjectId(task_id)})
    return result.deleted_count > 0
