import sys

from keras.preprocessing import image
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import SGD
from PIL import Image
import PIL.ImageOps

model = Sequential()
model.add(Dense(units=128, activation="relu", input_shape=(784,)))
model.add(Dense(units=128, activation="relu"))
model.add(Dense(units=128, activation="relu"))
model.add(Dense(units=10, activation="softmax"))

model.compile(optimizer=SGD(0.1), loss="categorical_crossentropy", metrics=["accuracy"])
model.load_weights("numbers.h5")
model._make_predict_function()


def preprocess(filename):
    png = Image.open(filename)
    png.load()

    img = Image.new("RGB", png.size, (255, 255, 255))
    img.paste(png, mask=png.split()[3])
    img = PIL.ImageOps.invert(img).convert("L")

    img = img.resize((28, 28))
    img = image.img_to_array(img)
    img = img.astype("float32") / 255
    img = img.reshape((1, 784))
    return img

def guess_number(filename):
    print("Guessing", filename)

    image = preprocess(filename)
    img_class = model.predict_classes(image)
    classname = img_class[0]

    print("My guess is", classname)
    return int(classname)


def bulk_guess_numbers(filenames):
    for filename in filenames:
        guess_number(filename)


if __name__ == "__main__":
    bulk_guess_numbers(sys.argv[1:])
