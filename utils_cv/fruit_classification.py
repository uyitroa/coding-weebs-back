'''
Ce code créé un réseau de neurones à partir de Resnet50 et s'entraîne sur les crop_clean
'''

from keras.applications import ResNet50
import numpy as np
from utils_cv.load_data import *
import os
import tensorflow as tf
from tensorflow import keras
from utils_cv.image_processing import *

DATASET_PATH = "database/dataset_fruits-type"

SEED = 42
BATCH_SIZE = 64

VALIDATION_PROP = 0.1

id_to_label = {}
label_to_id = {}
nbClasses = 0


def init():
    np.random.seed(SEED)


def createDictLabel():
    global id_to_label
    global label_to_id
    global nbClasses

    id_to_label.clear()
    label_to_id.clear()
    nbClasses = 0

    for folderName in os.listdir(DATASET_PATH):
        folderPath = os.path.join(DATASET_PATH, folderName)

        if os.path.isfile(folderPath):
            continue

        id_to_label[nbClasses] = folderName
        label_to_id[folderName] = nbClasses

        nbClasses += 1


def unison_shuffled_copies(a, b):
    p = np.random.permutation(len(a))
    return a[p], b[p]


def load_images():
    x = []
    y = []
    for folderName in os.listdir(DATASET_PATH):
        folderPath = os.path.join(DATASET_PATH, folderName)
        cropCleanPath = os.path.join(folderPath, "crop_clean")

        for fileName in os.listdir(cropCleanPath):
            if not fileName.endswith(".jpg"):
                continue
            filePath = os.path.join(cropCleanPath, fileName)
            x.append(np.array(load_image(filePath)))
            print("Ouverture", filePath, "de format", x[-1].shape)
            y.append(label_to_id[folderName])

    x = np.array(x)
    y = np.array(y)

    x, y = unison_shuffled_copies(x, y)
    return x, y


def separate_images(x, y):
    nbImgs = len(x)
    middle = int(nbImgs * VALIDATION_PROP)
    x_valid, y_valid = x[:middle], y[:middle]
    x_train, y_train = x[middle:], y[middle:]
    return x_train, y_train, x_valid, y_valid


if __name__ == "__main__":
    init()
    createDictLabel()

    x, y = load_images()
    x_train, y_train, x_valid, y_valid = separate_images(x, y)

    # mis en place du model : resnet + 2 couches denses
    model = tf.keras.Sequential()
    model.add(ResNet50(include_top=False,
                       input_shape=(100, 100, 3), pooling='avg'))

    model.add(tf.keras.layers.Dense(256, activation='relu'))
    model.add(tf.keras.layers.Dense(nbClasses, activation='softmax'))

    model.layers[0].trainable = False
    model.compile(loss=keras.losses.SparseCategoricalCrossentropy(),
                  optimizer=keras.optimizers.Adam(0.001),
                  metrics=['accuracy'])

    model.summary()

    model.fit(
        x=x_train,
        y=y_train,
        batch_size=BATCH_SIZE,
        validation_data=(x_valid, y_valid),
        epochs=1,
        verbose=1)

    model.save("fruits_classification_v1.h5")

label = ['apple_green',
         'apple_red',
         'apricot',
         'avocado',
         'banana',
         'clementine',
         'fig',
         'kiwi',
         'onion_red',
         'onion_white',
         'pear',
         'pepper_red',
         'potato',
         'strawberry',
         'watermelon']


def fruit_classify_manual(img, model=None):
    img = crop_manual(img)
    if model == None:
        model = keras.models.load_model("utils_cv/fruits_classification_v1.h5")
    resize = resize_image(img, (100, 100))
    sample = np.array([resize])
    pred = model.predict(sample)[0]
    ind_min = np.argmax(np.array(pred))

    return label[ind_min]


def fruit_classify(img, model=None):
    if model == None:
        model = keras.models.load_model("utils_cv/fruits_classification_v1.h5")
    resize = resize_image(img, (100, 100))
    sample = np.array([resize])
    pred = model.predict(sample)[0]
    ind_min = np.argmax(np.array(pred))

    return label[ind_min]
