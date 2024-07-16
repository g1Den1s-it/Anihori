from flask import request
from flask.blueprints import Blueprint
from anime.controlls import AnimeController

anime = Blueprint('anime', __name__)

anime_controller = AnimeController()


@anime.get('/list/')
def get_list():
    return anime_controller.get_all_anime()


@anime.get('/f')
def filter_list():
    filter_args = request.args.to_dict()
    return


@anime.get('/list/<int:id>/')
def get_detail(id):
    return anime_controller.get_detail_anime(id)


@anime.post('/list/favorite/')
def add_to_favorite():
    pass


@anime.post('/create/')
def create_anime():
    data = request.get_json()
    return anime_controller.create_anime(data)
