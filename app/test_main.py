from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_healthchecker():
    response = client.get("/api/healthchecker")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI with SQLAlchemy"}

def test_notes():
    response = client.post(
        "/api/notes/",
        headers = {},
        json = {
            "url": "/a"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "status": "success",
        "positive_feedback": 0,
        "negative_feedback": 0
    }

def test_notes_new_positive():
    response = client.post(
        "/api/notes/new",
        headers = {},
        json = {
            "url": "/test",
            "feedback": 1
        }
    )
    assert response.status_code == 201
    assert response.json()["status"] == "success"
