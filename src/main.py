import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.tasks import router as tasks_router
from src.api.auth import router as auth_router
from mangum import Mangum

app = FastAPI(
    title="Task Manager API",
    description="API for Task Management with JWT authentication and MongoDB.",
    version="1.0.0",
    openapi_prefix="/dev/"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

app.include_router(tasks_router)
app.include_router(auth_router)

handler = Mangum(app)
