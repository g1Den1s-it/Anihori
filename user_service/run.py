from auth import create_app
from config import Config

if "__main__" == __name__:
    create_app(Config).run(host='0.0.0.0', port=5000, debug=True)


