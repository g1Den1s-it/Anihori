from anime import db
from sqlalchemy.orm import relationship

anime_authors = db.Table(
    'anime_authors',
    db.Column('anime_id', db.Integer, db.ForeignKey('anime.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), primary_key=True)
)

anime_genres = db.Table(
    'anime_genres',
    db.Column('anime_id', db.Integer, db.ForeignKey('anime.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)


class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = db.Column(db.String(28), nullable=False, unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = db.Column(db.String(28), nullable=False, unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Series(db.Model):
    __tablename__ = 'series'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = db.Column(db.String(44), nullable=False)
    video = db.Column(db.String(164), nullable=False)
    position = db.Column(db.Integer, nullable=False)
    anime = db.Column(db.Integer, db.ForeignKey('anime.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "video": self.video,
            "position": self.position,
        }


class Anime(db.Model):
    __tablename__ = 'anime'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    authors = relationship('Author', secondary=anime_authors)
    create_at = db.Column(db.Date)
    genres = relationship('Genre', secondary=anime_genres)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "author": [
                author.to_dict() for author in self.authors
            ],
            "create_at": self.create_at,
            "genres": [
                genre.to_dict() for genre in self.genres
            ]
        }
