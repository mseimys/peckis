import os

from flask import Flask
from flask_cors import CORS


def initialize(config):
    if not os.path.exists(config["UPLOAD_FOLDER"]):
        os.makedirs(config["UPLOAD_FOLDER"])


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    initialize(app.config)

    from api import api

    app.register_blueprint(api)

    return app
