import pytest
from backend.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"CopyCat backend is running" in response.data


def test_submit_empty_input(client):
    response = client.post("/submit", json={"text": ""})
    assert response.status_code == 400
    assert response.get_json()["message"] == "No code submitted."


def test_submit_valid_code(client):
    test_code = "user_input = input()\neval(user_input)"
    response = client.post("/submit", json={"text": test_code})

    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data