import pytest
from tests.conftest import client, db


def test_create_anime(client):
    test_data = {
        "title": "fantastic",
        "description": "something",
        "create_at": "2011-06-06",
        "genres": ["fantastic"],
        "authors": ["David"]
    }

    response = client.post("/create/", json=test_data)

    assert response.status_code == 200
    assert response.json['title'] == "fantastic"
    assert response.json['description'] == "something"
    assert response.json['create_at'] == "Mon, 06 Jun 2011 00:00:00 GMT"


def test_get_list(client):
    test_data = {
        "title": "fantastic",
        "description": "something",
        "create_at": "2011-06-06",
        "genres": ["fantastic"],
        "authors": ["David"]
    }
    test_data_2 = {
        "title": "fantastic_2",
        "description": "something_2",
        "create_at": "2011-06-06",
        "genres": ["fantastic"],
        "authors": ["David"]
    }

    client.post("/create/", json=test_data)
    client.post("/create/", json=test_data_2)

    response = client.get("/list/")

    assert response.status_code == 200

    assert response.json[0]['title'] == "fantastic"
    assert response.json[0]['description'] == "something"
    assert response.json[0]['create_at'] == "Mon, 06 Jun 2011 00:00:00 GMT"

    assert response.json[1]['title'] == "fantastic_2"
    assert response.json[1]['description'] == "something_2"
    assert response.json[1]['create_at'] == "Mon, 06 Jun 2011 00:00:00 GMT"


def test_filter_list(client):
    test_data = {
        "title": "fantastic",
        "description": "something",
        "create_at": "2011-06-06",
        "genres": ["horror"],
        "authors": ["David"]
    }
    test_data_2 = {
        "title": "fantastic_2",
        "description": "something_2",
        "create_at": "2011-06-06",
        "genres": ["fantastic"],
        "authors": ["David"]
    }

    client.post("/create/", json=test_data)
    client.post("/create/", json=test_data_2)

    response = client.get("/list/f?title=fantastic")

    assert response.status_code == 200

    assert response.json[0]['title'] == "fantastic"
    assert response.json[0]['description'] == "something"
    assert response.json[0]['create_at'] == "Mon, 06 Jun 2011 00:00:00 GMT"


def test_get_detail(client):
    test_data = {
        "title": "fantastic",
        "description": "something",
        "create_at": "2011-06-06",
        "genres": ["horror"],
        "authors": ["David"]
    }

    res = client.post("/create/", json=test_data)

    response = client.get(f"/list/{res.json['id']}/")

    assert response.status_code == 200

    assert response.json['title'] == "fantastic"
    assert response.json['description'] == "something"
    assert response.json['create_at'] == "Mon, 06 Jun 2011 00:00:00 GMT"
    assert response.json['series'] == []
