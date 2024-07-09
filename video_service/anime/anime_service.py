from anime import db
from anime.models import Anime, Author, Genre, Series


class AnimeService:
    def get_series(self, anime_id: int) -> Series | Exception:
        try:
            series = Series.query.filter(anime=anime_id)

            return series
        except Exception as e:
            db.session.rollback()

            return e

    def get_anime(self, anime_id) -> Anime | Exception:
        try:
            anime = Anime.query.get(id=anime_id)

            return anime
        except Exception as e:
            db.session.rollback()
            return e

    def post_add_video_to_anime(self, instance: dict) -> Series | Exception:
        try:
            series = Series(
                name=instance['name'],
                vidoe=instance['video'],
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

    def post_create_anime(self, instance: dict) -> Anime | Exception:
        try:
            genre = self.get_or_create_genre(name=instance['genre'])
            author = self.get_or_create_author(name=instance['author'])

            anime = Anime(
                title=instance['title'],
                description=instance['description'],
                create_at = instance['create_at']
            )
            anime.author.append(author)
            anime.genre.append(genre)

            db.session.add(Anime)
            db.session.commit()

            return Anime

        except Exception as e:
            db.session.rollback()
            return e


    def get_or_create_author(self, **kwargs) -> Author:
        try:
            author = Author.query.get(name=kwargs.get('name'))

            return author
        except:
            db.session.rollback()

            author = Author(name=kwargs.get('name'))

            db.session.add(author)
            db.session.commit()

            return author

    def get_or_create_genre(self, **kwargs) -> Genre:
        try:
            genre = Genre.query.get(name=kwargs.get('name'))

            return genre
        except:
            db.session.rollback()

            genre = Genre(name=kwargs.get('name'))

            db.session.add(genre)
            db.session.commit()

            return genre
