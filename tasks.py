import requests
from PIL import Image
import PIL.ImageOps

from app import celery
from config import Config


def preprocess(filename):
    import tensorflow as tf

    png = Image.open(filename)
    png.load()

    img = Image.new("RGB", png.size, (255, 255, 255))
    img.paste(png, mask=png.split()[3])
    img = PIL.ImageOps.invert(img).convert("L")

    img = img.resize((28, 28))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = img.astype("float32") / 255
    img = img.reshape((1, 784))
    return img


@celery.task()
def guess_number(filename):
    image = preprocess(filename)
    response = requests.post(Config.SERVING_NUMBER, json={"instances": image.tolist()})
    predictions = response.json().get("predictions", [])[0]
    classname = predictions.index(max(predictions))

    print(f"My guess is {classname}")
    return int(classname)
