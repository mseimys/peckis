import random

import numpy as np
import keras
from keras.preprocessing import image
from keras.datasets import mnist
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import SGD
from keras.callbacks import LearningRateScheduler


from .utils import cv2_clipped_zoom

MODEL_LOCATION = "weights/numbers.h5"


class NumberModel(Sequential):
    def __init__(self):
        super().__init__()
        self.add(Dense(units=128, activation="relu", input_shape=(784,)))
        self.add(Dense(units=128, activation="relu"))
        self.add(Dense(units=128, activation="relu"))
        self.add(Dense(units=10, activation="softmax"))

    def initialize(self):
        self.load_weights(MODEL_LOCATION)
        self._make_predict_function()
        return self


def train_and_save_number_model(save_location):
    (train_x, train_y), (test_x, test_y) = mnist.load_data()

    train_x = train_x.astype("float32") / 255
    test_x = test_x.astype("float32") / 255

    # Take the same images and zoom in, to create more training data
    zoomed_x = np.array([cv2_clipped_zoom(train_x[index], random.randrange(120, 140) / 100.0) for index in range(30000)])
    zoomed_y = train_y[:30000]

    train_x = np.append(train_x, zoomed_x, axis=0)
    train_y = np.append(train_y, zoomed_y, axis=0)

    train_x = train_x.reshape(60000 + len(zoomed_x), 784)
    test_x = test_x.reshape(10000, 784)

    train_y = keras.utils.to_categorical(train_y, 10)
    test_y = keras.utils.to_categorical(test_y, 10)

    def lr_schedule(epoch):
        lr = 0.1
        if epoch > 15:
            lr = lr / 100
        elif epoch > 10:
            lr = lr / 10
        elif epoch > 5:
            lr = lr / 5
        print("Learning Rate: ", lr)
        return lr

    model = NumberModel()

    model.compile(optimizer=SGD(lr_schedule(0)), loss="categorical_crossentropy", metrics=["accuracy"])

    lr_scheduler = LearningRateScheduler(lr_schedule)
    model.fit(train_x, train_y, batch_size=32, epochs=10, shuffle=True, verbose=1, validation_split=0.1, callbacks=[lr_scheduler])

    accuracy = model.evaluate(x=test_x, y=test_y, batch_size=32)

    print("Model accuracy: ", accuracy[1])

    model.save(save_location)


if __name__ == "__main__":
    train_and_save_number_model(MODEL_LOCATION)
