from anime.anime_service import AnimeService
from anime.schemas import AnimeSchema
from flask import Response, jsonify
from marshmallow import ValidationError


class AnimeController:
    def __init__(self):
        self.anime_service = AnimeService()

    def get_all_anime(self) -> tuple[Response, int]:
        anime_list = self.anime_service.get_all_anime_from_db()

        return jsonify([{ani.to_dict()} for ani in anime_list]), 200

    def get_detail_anime(self, anime_id: int) -> tuple[Response, int]:
        anime = self.anime_service.get_anime(anime_id)
        series = self.anime_service.get_series(anime_id)

        json = anime.to_dict()
        json["series"] = [{seria} for seria in series]

        return jsonify(json), 200

    def create_anime(self, data: dict) -> tuple[Response, int]:
        if not data:
            return jsonify({"message": "No data provided"}), 400

        anime_schema = AnimeSchema()

        try:
            valid_data = anime_schema.load(data)

            anime = self.anime_service.post_create_anime(valid_data)

            return jsonify(anime.to_dict()), 200

        except ValidationError as err:

            return jsonify(err.messages), 422

