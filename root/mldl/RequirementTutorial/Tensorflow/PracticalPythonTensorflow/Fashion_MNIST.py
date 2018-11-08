#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np

# tensorflow version
print("Tensorflow version :", tf.__version__)

# Import the Fashion MNIST dataset
fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dree', 'Coat', 'Sandal', 'Shift', 'Sneaker', 'Bag', 'Ankle boot']

# Preprocess the data
train_images , test_images = train_images / 255.0 , test_images / 255.0

## Build the model

#Setup the layers
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

# Compile the model
model.compile(
        optimizer=tf.train.AdamOptimizer(),
        loss='sparse_categorical_crossentropy',
        metrics=['acuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=5)


# Evaluate accuracy
test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)
