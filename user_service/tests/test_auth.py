import pytest
from tests.conftest import app, client


def test_registration_user(client):
    test_data = {
        "username": "David",
        "email": "david@test.com",
        "password": "davidqwerty!qw"
    }

    response = client.post("/api/register/", json=test_data)
    test_data.pop("password")
    assert response.status_code == 200
    for k, v in test_data:
        assert response.json[k] == v


def test_registration_user_with_wrong_data(client):
    test_data = {
        "user": "david",
        "email": "t@t.com",
        "password": "wertyu"
    }

    response = client.post("/api/register/", json=test_data)

    assert response.status_code == 400
