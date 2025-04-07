import os
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.config import db, client
import asyncio

os.environ["TESTING"] = "True"

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def test_app():
    with TestClient(app) as client:
        yield client

@pytest.fixture
async def async_test_app():
    async with TestClient(app) as client:
        yield client

@pytest.fixture(autouse=True)
async def clean_db():
    """Clean database before and after each test"""
    collections = await db.list_collection_names()
    for collection in collections:
        await db[collection].delete_many({})
    yield
    collections = await db.list_collection_names()
    for collection in collections:
        await db[collection].delete_many({})