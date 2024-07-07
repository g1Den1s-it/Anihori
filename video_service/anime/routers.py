from flask.blueprints import Blueprint

media = Blueprint('anime', __name__)


@media.post('/list/')
def get_list():
    pass


@media.post('/create/')
def add_to_favorite():
    pass
