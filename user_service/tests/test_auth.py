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
    for k, v in test_data.items():
        assert response.json[k] == v


def test_registration_user_with_wrong_data(client):
    test_data = {
        "user": "david",
        "email": "t@t.com",
        "password": "wertyu"
    }

    response = client.post("/api/register/", json=test_data)

    assert response.status_code == 400


def test_login_and_login_verification(client):
    test_data = {
        "username": "David",
        "email": "david@test.com",
        "password": "davidqwerty!qw"
    }
    response = client.post("/api/register/", json=test_data)

    assert response.status_code == 200

    login_response = client.post("/api/login/", json=test_data)

    assert login_response.status_code == 200
    assert 'access' in login_response.json
    assert 'refresh' in login_response.json

    access_token = login_response.json['access']
    refresh_token = login_response.json['refresh']

    access_response = client.get("/api/login-verification/", headers={"Authorization": f"Bearer {access_token}"})
    refresh_response = client.get("/api/login-verification/", headers={"Authorization": f"Bearer {refresh_token}"})
    invalid_response = client.get("/api/login-verification/", headers={"Authorization": "Bearer dq19e12dj120"})

    assert access_response.status_code == 200
    assert refresh_response.status_code == 200
    assert invalid_response.status_code == 401
    assert "Valid" in access_response.json['message']
    assert "Valid" in refresh_response.json['message']
    assert "Invalid" in invalid_response.json['message']


def test_profile(client):
    test_data = {
        "username": "David",
        "email": "david@test.com",
        "password": "davidqwerty!qw"
    }
    response = client.post("/api/register/", json=test_data)

    assert response.status_code == 200

    login_response = client.post("/api/login/", json=test_data)

    assert login_response.status_code == 200

    new_data = {
        "username": "john",
        "email": 'john@test.com'
    }

    profile_response = client.put(
        "/api/profile/",
        json=new_data,
        headers={"Authorization": f"Bearer {login_response.json['access']}"}
    )

    assert profile_response.status_code == 200
    for k, v in new_data.items():
        assert profile_response.json[k] == v
