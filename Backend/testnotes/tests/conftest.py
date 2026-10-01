import pytest
from fastapi.testclient import TestClient

from main import app, blogs


@pytest.fixture
def client():
    blogs[:] = [
        {"id": 1, "title": "Python", "content": "Learn Python"},
        {"id": 2, "title": "FastAPI", "content": "Learn FastAPI"}
    ]

    with TestClient(app) as test_client:
        yield test_client