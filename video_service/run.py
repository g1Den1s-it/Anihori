from anime import create_app
from config import Config

if '__main__' == __name__:
    app = create_app(Config)
    app.run(host='0.0.0.0', port=5001)
