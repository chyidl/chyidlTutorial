#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# import the necessary packages
from sklearn.preprocessing import LabelBinarizer        # The LabelBinaries will be used to one-hot encode our integer labels as vector labels
from sklearn.model_selection import train_test_split    # used to create our training and testing splits from the MNIST dataset
from sklearn.metrics import classification_report       # give us a nicely formatted report displaying the total accuracy of our model
from keras.models import Sequential                     # indicates that our network will be feedforward and layers will be added to the class sequentially
from keras.layers.core import Dense                     # implementation of our fully-connected layers
from keras.optimizers import SGD                        # optimize the parameters of the network
from sklearn import datasets                            # gain access to full MNIST dataset
import matplotlib.pyplot as plt
import numpy as np
import argparse


# Construct the argument parse and parse the arguments
# figure plotting the loss and accuracy over time will be saved to disk
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
                help="path to the output loss/accuracy plot")
args = vars(ap.parse_args())


# grab the MNIST dataset (if this is your first time running this
# script, the download may take a minute -- the 55MB MNIST dataset
# will be downloaded)
print("[INFO] loading MNIST (full) dataset...")
dataset = datasets.fetch_mldata("MNIST Original")


# scale the raw pixel intensities to the range [0, 1.0], then
# construct the training and testing splits
data = dataset.data.astype("float") / 255.0         # normalization
(trainX, testX, trainY, testY) = train_test_split(data,
                                                   dataset.target, test_size=0.25)


# convert the labels from integers to vectors
# transform these integer labels into vector labels, where the index in the vector for label is set to 1 and 0 otherwise (this process is called one-hot encoding)
lb = LabelBinarizer()
trainY = lb.fit_transform(trainY)
testY = lb.transform(testY)


# define our network architecture
model = Sequential()
model.add(Dense(256, input_shape=(784,), activation="sigmoid"))
model.add(Dense(128, activation="sigmoid"))
model.add(Dense(10, activation="softmax"))


# train the model using SGD
print("[INFO] training network...")
sgd = SGD(0.01)  # learning rate of 0.01
model.compile(loss="categorical_crossentropy", optimizer=sgd,
              metrics=["accuracy"])
# which we'll use to plot the loss/accuracy of the network overtime in a couple of code blocks
H = model.fit(trainX, trainY, validation_data=(testX, testY),
              epochs=100, batch_size=128)

# evaluate the network
print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=128)
print(classification_report(testY.argmax(axis=1),
                            predictions.argmax(axis=1),
                            target_names=[str(x) for x in lb.classes_]))

# plot the training loss and accuracy
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, 100), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, 100), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, 100), H.history["acc"], label="train_acc")
plt.plot(np.arange(0, 100), H.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.savefig(args["output"])
