import tensorflow as tf

from PIL import Image
import PIL.ImageOps

from app import celery
from models.numbers import NumberModel

model = NumberModel().initialize()


def preprocess(filename):
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
    print(f"Guessing {filename}")

    image = preprocess(filename)
    img_class = model.predict_classes(image)
    classname = img_class[0]

    print(f"My guess is {classname}")
    return int(classname)
