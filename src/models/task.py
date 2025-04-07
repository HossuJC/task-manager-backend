from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TaskStatus(str, Enum):
    """
    Enumeration of the possible task statuses.
    
    **Values:**
    - **todo:** The task has not started yet.
    - **in_progress:** The task is in progress.
    - **completed:** The task has been completed.
    """
    todo = "todo"
    in_progress = "in_progress"
    completed = "completed"

class Task(BaseModel):
    """
    Data model for task management.
    
    **Attributes:**
    - **title (str):** Title of the task.
    - **description (Optional[str]):** Optional description of the task.
    - **status (TaskStatus):** Status of the task (default: "todo").
    """
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.todo
