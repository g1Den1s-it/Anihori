from anime import db
from anime.models import Anime, Author, Genre, Series
from anime.models import user_anime
from sqlalchemy import Table, select


class AnimeService:
    def get_series(self, anime_id: int) -> Series | Exception:
        try:
            series = Series.query.filter(Series.anime == anime_id).all()

            return series
        except Exception as e:
            db.session.rollback()

            return e

    def get_anime(self, anime_id) -> Anime | Exception:
        try:
            anime = Anime.query.get(anime_id)

            return anime
        except Exception as e:
            db.session.rollback()
            return e

    def post_add_video_to_anime(self, instance: dict) -> Series | Exception:
        try:
            series = Series(
                name=instance['name'],
                video=instance['video'],
                anime=instance['anime']
            )

            db.session.add(series)
            db.session.commit()

        except Exception as e:
            db.session.rollback()

            return e

    def get_all_anime_from_db(self) -> list[Anime] | Exception:
        try:
            anime = Anime.query.all()
            return anime

        except Exception as e:
            db.session.rollback()
            return e

    def anime_filter(self, **kwargs) -> list[Anime] | Exception:
        try:
            author_name = kwargs.get("author")
            genre_name = kwargs.get("genres")
            anime_filters = {
                "title": kwargs.get("title"),
                "create_at": kwargs.get("date")
            }
            query = Anime.query

            if author_name:
                author = Author.query.filter_by(name=author_name).first()
                if author:
                    query = query.filter(Anime.authors.contains(author))

            if genre_name:
                genres = Genre.query.filter_by(name=genre_name).first()
                if genres:
                    query = query.filter(Anime.genres.contains(genres))

            for key, value in anime_filters.items():
                if value:
                    query = query.filter(getattr(Anime, key) == value)

            anime = query.all()

            return anime

        except Exception as e:
            return e

    def post_create_anime(self, instance: dict) -> Anime | Exception:
        try:
            genre_list = []
            for genre in instance['genres']:
                genre_list.append(self.get_or_create_genre(genre))

            authors_list = []
            for author in instance['authors']:
                authors_list.append(self.get_or_create_author(author))

            anime = Anime(
                title=instance['title'],
                description=instance['description'],
                create_at=instance['create_at']
            )
            anime.authors.extend(authors_list)
            anime.genres.extend(genre_list)

            db.session.add(anime)
            db.session.commit()

            return anime

        except Exception as e:
            db.session.rollback()
            return e


    def get_or_create_author(self, name) -> Author:
        try:
            author = Author.query.filter_by(name=name).first()
            if author:
                return author

            author = Author(name=name)

            db.session.add(author)
            db.session.commit()

            return author
        except:
            db.session.rollback()

            author = Author.query.filter_by(name=name).first()
            return author

    def get_or_create_genre(self, name) -> Genre:
        try:
            genre = Genre.query.filter_by(name=name).first()

            if genre:
                return genre

            genre = Genre(name=name)

            db.session.add(genre)
            db.session.commit()

            return genre
        except:
            db.session.rollback()

            genre = Genre.query.filter_by(name=name).first()
            return genre


    def create_seria(self, instance: dict) -> Series | Exception:
        try:
            series = Series(
                name=instance['name'],
                video=instance['video'],
                anime=instance['anime']
            )

            db.session.add(series)
            db.session.commit()

            return series

        except Exception as e:
            db.session.rollback()
            return e


    def post_favorite(self, user_id: int, anime_id: int) -> Table | Exception:
        try:
            favorite = user_anime.insert().values(user_id=user_id, anime_id=anime_id)

            db.session.execute(favorite)
            db.session.commit()

            return favorite

        except Exception as e:

            db.session.rollback()
            return e


    def get_list_favorite(self, user_id: int) -> list[Anime] | Exception:
        try:
            anime_ids = db.session.query(user_anime.c.anime_id).filter_by(user_id=user_id).all()

            anime_ids = [anime_id for (anime_id,) in anime_ids]

            anime_list = Anime.query.filter(Anime.id.in_(anime_ids)).all()

            return anime_list

        except Exception as e:
            db.session.rollback()
            return e

    def remove_anime_from_favorite(self, user_id: int, anime_id: int) -> bool | Exception:
        try:
            db.session.execute(
                user_anime.delete().where(
                    (user_anime.c.user_id == user_id) &
                    (user_anime.c.anime_id == anime_id)
                )
            )
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e

    def is_favorite_anime(self, user_id: int, anime_id: int) -> bool:
        try:
            exists = db.session.query(
                db.exists().where(
                    (user_anime.c.user_id == user_id) &
                    (user_anime.c.anime_id == anime_id)
                )
            ).scalar()

            return exists
        except Exception as e:
            db.session.rollback()
            return False
