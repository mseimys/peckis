import requests

from app import celery
from config import Config
from utils.preprocess import preprocess


@celery.task()
def guess_number(filename):
    image = preprocess(filename)
    response = requests.post(Config.SERVING_NUMBER, json={"instances": image.tolist()})
    predictions = response.json().get("predictions", [])[0]
    classname = predictions.index(max(predictions))

    print(f"My guess is {classname}")
    return int(classname)
