from flask import request
from flask.blueprints import Blueprint
from anime.controlls import AnimeController

anime = Blueprint('anime', __name__)

anime_controller = AnimeController()


@anime.get('/list/')
def get_list():
    return anime_controller.get_all_anime()


@anime.get('/list/f')
def filter_list():
    filter_args = request.args.to_dict()
    return anime_controller.get_anime_by_filters(**filter_args)


@anime.get('/list/<int:id>/')
def get_detail(id):
    return anime_controller.get_detail_anime(id)


@anime.post('/list/<int:id>/favorite/')
def add_to_favorite(id):
    token = request.headers["Authorization"]
    return anime_controller.post_to_favorite(token, id)


@anime.post('/create/')
def create_anime():
    data = request.get_json()
    return anime_controller.create_anime(data)
