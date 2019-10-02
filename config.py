import os

ROOT_DIR = os.path.dirname(__file__)


class Config:
    UPLOAD_FOLDER = os.path.join(ROOT_DIR, "uploads")
    ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])

    CELERY_RESULT_BACKEND = "db+sqlite:///" + os.path.join(ROOT_DIR, "celery_results.db")
    CELERY_BROKER_URL = "sqla+sqlite:///" + os.path.join(ROOT_DIR, "celery.db")
    CELERYD_CONCURRENCY = 2

    SERVING_NUMBER = "http://localhost:8501/v1/models/number:predict"
