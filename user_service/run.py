from auth import create_app


if "__main__" == __name__:
    create_app().run(host='0.0.0.0', port=5000, debug=True)


