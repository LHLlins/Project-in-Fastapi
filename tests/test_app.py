from http import HTTPStatus

from fastapi.testclient import TestClient

from app import app


def test_root_deve_retornar_ok():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello World"}


def test_create_user():
    client = TestClient(app)

    response = client.post(
        "/users/",
        json={
            "username": "testusername",
            "password": "testpassword",
            "email": "test@testemail",
        },
    )
    # Validate
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "testusername",
        "password": "testpassword",
        "email": "test@testemail",
        "id": 1,
    }
