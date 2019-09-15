import os

from flask import Flask
from flask_cors import CORS

from celery import Celery
from config import Config


def initialize(config):
    if not os.path.exists(config["UPLOAD_FOLDER"]):
        os.makedirs(config["UPLOAD_FOLDER"])


celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)

    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)

    initialize(app.config)
    celery.conf.update(app.config)

    from api import api

    app.register_blueprint(api)

    return app

