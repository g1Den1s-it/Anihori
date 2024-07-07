from flask.blueprints import Blueprint

anime = Blueprint('anime', __name__)


@anime.post('/list/')
def get_list():
    pass


@anime.post('/create/')
def add_to_favorite():
    pass
