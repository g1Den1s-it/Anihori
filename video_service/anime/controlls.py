import os
import requests
import jwt
from anime.anime_service import AnimeService
from anime.schemas import AnimeSchema, SeriesSchema
from flask import Response, jsonify
from config import Config
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


class AnimeController:
    def __init__(self):
        self.anime_service = AnimeService()

    def get_all_anime(self) -> tuple[Response, int]:
        anime_list = self.anime_service.get_all_anime_from_db()

        return jsonify([ani.to_dict() for ani in anime_list]), 200

    def get_detail_anime(self, anime_id: int) -> tuple[Response, int]:
        try:
            anime = self.anime_service.get_anime(anime_id)
            series = self.anime_service.get_series(anime_id)

            if isinstance(anime, Exception):
                raise anime
            if isinstance(series, Exception):
                raise series

            json = anime.to_dict()
            json["series"] = [seria.to_dict() for seria in series]

            return jsonify(json), 200

        except Exception as e:
            return jsonify(str(e)), 500

    def create_anime(self, data: dict) -> tuple[Response, int]:
        if not data:
            return jsonify({"message": "No data provided"}), 400

        anime_schema = AnimeSchema()

        try:
            valid_data = anime_schema.load(data)

            anime = self.anime_service.post_create_anime(valid_data)

            if isinstance(anime, Exception):
                raise anime

            return jsonify(anime.to_dict()), 200

        except Exception as e:
            return jsonify({"message": str(e)}), 400

    def post_to_favorite(self, uid: int, auth_token: str) -> tuple[Response, int]:
        try:
            if not uid:
                return jsonify({"message": "not found anime"}), 400

            if self.check_authorization(auth_token) != 200:
                return jsonify({"message": "user is not authorized"}), 401
            else:
                decode = jwt.decode(auth_token.split(" ")[1], options={"verify_signature": False})

                if self.anime_service.is_favorite_anime(decode['sub'], uid):
                    return jsonify({"message": "Anime already added to favorites"}), 200

                user_anime = self.anime_service.post_favorite(decode['sub'], uid)

                if isinstance(user_anime, Exception):
                    raise user_anime

                return jsonify({"message": "success"}), 200

        except Exception as e:
            return jsonify({"message": str(e)}), 500

    def get_favorite_list(self, auth_token: str) -> tuple[Response, int]:
        try:
            if self.check_authorization(auth_token) != 200:
                return jsonify({"message": "user is not authorized"}), 401
            else:
                decode = jwt.decode(auth_token.split(" ")[1], options={"verify_signature": False})
                favorite_list = self.anime_service.get_list_favorite(decode['sub'])

                if isinstance(favorite_list, Exception):
                    raise favorite_list

                return jsonify([anime.to_dict() for anime in favorite_list]), 200

        except Exception as e:
            return jsonify({"message": str(e)}), 500

    def remove_favorite(self, uid: int, auth_token: str) -> tuple[Response, int]:
        try:
            if not uid:
                return jsonify({"message": "not found anime"}), 400

            if self.check_authorization(auth_token) != 200:
                return jsonify({"message": "user is not authorized"}), 401
            else:
                decode = jwt.decode(auth_token.split(" ")[1], options={"verify_signature": False})

                if not self.anime_service.is_favorite_anime(decode['sub'], uid):
                    return jsonify({"message": f"User {decode['sub']} does not have anime {uid} in their favorites."}), 400

                is_remove = self.anime_service.remove_anime_from_favorite(decode['sub'], uid)

                if isinstance(is_remove, Exception):
                    raise is_remove

                return jsonify({"message": "removed"}), 200

        except Exception as e:

            return jsonify({"message": str(e)}), 500

    def get_anime_by_filters(self, **kwargs) -> tuple[Response, int]:
        try:
            anime = self.anime_service.anime_filter(**kwargs)

            if isinstance(anime, Exception):
                raise anime

            return jsonify([ani.to_dict() for ani in anime]), 200

        except Exception as e:
            return jsonify({"message": str(e)}), 400

    def create_seria_to_anime(self, instance: dict, file: FileStorage) -> tuple[Response, int]:
        if not instance:
            return jsonify({"message": "No data provided!"}), 400

        if not file:
            return jsonify({'message': "Video must be required!"}), 400

        try:
            series_schema = SeriesSchema()

            valid_data = series_schema.load(instance)

            filename = secure_filename(file.filename.lower())

            if file and self.allowed_file(filename):

                media_folder = os.path.join(Config.UPLOAD_FOLDER, 'media')

                if not os.path.isdir(media_folder):
                    os.mkdir(media_folder)

                file_path = os.path.join(media_folder, filename)

                file.save(file_path)
                series = self.anime_service.create_seria(valid_data, file_path)

                if isinstance(series, Exception):
                    raise series

                return jsonify(series.to_dict()), 200
            else:
                return jsonify({"message": f"unsupported type of file {file.filename}"}), 400
        except Exception as e:
            return jsonify({"message": e}), 400

    @staticmethod
    def allowed_file(file) -> bool:
        return '.' in file and file.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

    @staticmethod
    def check_authorization(full_token: str) -> int:
        res = requests.get('http://auth:5000/api/login-verification/',
                           headers={"Authorization": full_token})

        return res.status_code
