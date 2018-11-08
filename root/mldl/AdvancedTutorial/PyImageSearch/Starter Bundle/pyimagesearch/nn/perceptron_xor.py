#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Evaluating the Perceptron Bitwise Datasets

# import the necessary packages
from perceptron import Perceptron
import numpy as np


# construct the OR dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# define our perceptron and train it
print("[INFO] training perceptron...")
p =Perceptron(X.shape[1], alpha=0.1)
p.fit(X, y, epochs=20)


# Now that our perceptron is trained we can evaluate it
print("[INFO] testing perceptron...")

# Now that our network is trained, loop over the data points
for (x, target) in zip(X, y):
    # make a prediction on the data point and display the result
    # to our console
    pred = p.predict(x)
    print("[INFO] data={}, ground-truth={}, pred={}".format(x, target[0], pred))

"""
    No matter how many times you run this experiment with varying learning rates or different
weight initialization schemes, you will never be able to correctly model the XOR function with a 
single layer Perceptron. Instead, what we need is more layers - and with that, comes the start of deep learning
"""