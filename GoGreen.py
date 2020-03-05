from __future__ import print_function
import keras
from keras.models import Model
from keras.layers import Dense, Conv2D, BatchNormalization, Activation
from keras.layers import AveragePooling2D, Input, Flatten, Dropout
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, LearningRateScheduler
from keras.callbacks import ReduceLROnPlateau
from keras.preprocessing.image import ImageDataGenerator
from keras.regularizers import l2
from keras import backend as K
import os, cv2, re, random
import numpy as np
#import pandas as pd
from keras.preprocessing.image import img_to_array, load_img
from keras import layers, models, optimizers
from sklearn.model_selection import train_test_split

model = keras.applications.resnet.ResNet50(weights='imagenet', include_top=False, input_shape=(64, 64, 3))
y = model.output
y = Flatten()(y)
y = Dropout(0.5)(y)
y = Dense(3, activation='softmax', name='class_id')(y)
new_model = Model(inputs=model.input, outputs=y)
new_model.compile(loss="categorical_crossentropy",
              optimizer="rmsprop",
              metrics=["accuracy"])

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        'data/Train',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
        'data/Test',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')

new_model.fit_generator(
        train_generator,
        steps_per_epoch=2000,
        epochs=10,
        validation_data=validation_generator,
        validation_steps=800)
new_model.save("model.h5")