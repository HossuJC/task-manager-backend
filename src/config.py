import os
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str = os.getenv("DB_STRING")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_TEST_NAME: str = os.getenv("DB_TEST_NAME")

settings = Settings()

client = AsyncIOMotorClient(settings.MONGO_URI)
db_name = settings.DB_TEST_NAME if os.getenv("TESTING") == "True" else settings.DB_NAME
db = client[db_name]
