from datetime import date

import pytest
from tests.conftest import client, db
from anime.models import Genre, Author, Series, Anime


def test_genre(db):
    genre = Genre(name="Romance")

    db.session.add(genre)
    db.session.commit()

    assert genre.id is not None
    assert genre.name == "Romance"
    assert genre.to_dict() == {
        "id": genre.id,
        "name": "Romance"
    }


def test_author(db):
    author = Author(name="John")

    db.session.add(author)
    db.session.commit()

    assert author.id is not None
    assert author.name == "John"
    assert author.to_dict() == {
        "id": author.id,
        "name": "John"
    }


def test_series(db):
    series = Series(
        name="Fade",
        video="/static/media/fade.mp4",
        position=1,
        anime=3
    )

    db.session.add(series)
    db.session.commit()

    assert series.id is not None
    assert series.name == "Fade"
    assert series.video == "/static/media/fade.mp4"
    assert series.position == 1
    assert series.anime == 3
    assert series.to_dict() == {
        "id": series.id,
        "name": "Fade",
        "video": "/static/media/fade.mp4",
        "position": 1,
    }


def test_anime(db):
    genre = Genre(name="Romance")
    author = Author(name="Hero")

    db.session.add(genre)
    db.session.add(author)
    db.session.commit()

    anime = Anime(
        title="Horimiya",
        description="On the surface, the thought of Kyouko Hori and Izumi Miyamura getting along would be the last thing in people's minds. " +
                    "After all, Hori has a perfect combination of beauty and brains, while Miyamura appears meek and distant to his fellow classmates. " +
                    "However, a fateful meeting between the two lays both of their hidden selves bare. Even though she is popular at school, Hori has little time to socialize with her friends due to housework. " +
                    "On the other hand, Miyamura lives under the noses of his peers, his body bearing secret tattoos and piercings that make him look like a gentle delinquent.",
        authors=[author],
        genres=[genre],
        create_at=date(2021, 10, 1)
    )

    db.session.add(anime)
    db.session.commit()

    assert anime.id is not None
    assert anime.title == "Horimiya"
    assert anime.description == "On the surface, the thought of Kyouko Hori and Izumi Miyamura getting along would be the last thing in people's minds. After all, Hori has a perfect combination of beauty and brains, while Miyamura appears meek and distant to his fellow classmates. However, a fateful meeting between the two lays both of their hidden selves bare. Even though she is popular at school, Hori has little time to socialize with her friends due to housework. On the other hand, Miyamura lives under the noses of his peers, his body bearing secret tattoos and piercings that make him look like a gentle delinquent."
    assert anime.create_at == date(2021, 10, 1)
    assert anime.to_dict() == {
        "id": anime.id,
        "title": "Horimiya",
        "description": "On the surface, the thought of Kyouko Hori and Izumi Miyamura getting along would be the last thing in people's minds. After all, Hori has a perfect combination of beauty and brains, while Miyamura appears meek and distant to his fellow classmates. However, a fateful meeting between the two lays both of their hidden selves bare. Even though she is popular at school, Hori has little time to socialize with her friends due to housework. On the other hand, Miyamura lives under the noses of his peers, his body bearing secret tattoos and piercings that make him look like a gentle delinquent.",
        "author": [{"id": author.id, "name": "Hero"}],
        "create_at": date(2021, 10, 1),
        "genres": [{"id": genre.id, "name": "Romance"}]
    }
