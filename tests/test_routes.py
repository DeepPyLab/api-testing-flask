import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Welcome to the API!"}


def test_get_resource(client):
    response = client.get("/api/v1/resource")
    assert response.status_code == 200
    assert response.get_json() == {"data": "Sample Data"}


def test_create_resource_success(client):
    response = client.post("/api/v1/resource", json={"name": "Test Resource"})
    assert response.status_code == 201
    assert response.get_json() == {
        "message": "Resource created",
        "data": {"name": "Test Resource"},
    }


def test_create_resource_failure(client):
    response = client.post("/api/v1/resource", json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid data"}
