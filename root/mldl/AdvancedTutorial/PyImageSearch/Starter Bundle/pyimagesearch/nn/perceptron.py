#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Implementing the Perceptron in Python3

# import the necessary packages
import numpy as np


# 感知器，which accepts a single required parameter followed by a second optional one:
class Perceptron:
    def __init__(self, N, alpha=0.01):
        """
        :param N:  The number of columns in our input feature vectors.
        :param alpha: Our learning rate for the Perceptron algorithm
        """
        # initialize the weight matrix and store the learning rate
        # The weight matrix will have N + 1 entries, one for each of N inputs in the feature vector, plus one for the bias
        self.W = np.random.randn(N + 1) / np.sqrt(N) # from a normal(Gaussian) distribution with zero mean and unit variance.
        self.alpha = alpha

    def step(self, x):
        # apply the step function
        return 1 if x > 0 else 0


    # fit a model to the data
    def fit(self, X, y, epochs=10):
        """
        :param X: actual training data
        :param y: target output class labels
        :param epochs: the number of epochs our Perceptron will train for
        :return:
        """
        # insert a column of 1's as the last entry in the feature
        # matrix -- this little trick allows us to treat the bias
        # as a trainable parameter within the weight matrix
        X = np.c_[X, np.ones((X.shape[0]))] # allow us to treat the bias as a trainable parameter directly directly inside the weight matrix

        # loop over the desired number of epochs
        for epoch in np.arange(0, epochs):
            # loop over each individual data point
            for (x, target) in zip(X, y):
                # take the dot product between the input features
                # and the weight matrix, then pass this value
                # through the step function to obtain the prediction
                p = self.step(np.dot(x, self.W))

                # only perform a weight update if our prediction
                # does not match the target
                if p != target:
                    # datermine the error
                    error = p - target

                    # update the weight matrix
                    self.W += -self.alpha * error * x

    def predict(self, X, addBias=True):
        # ensure our input is a matrix
        X = np.atleast_2d(X)

        # check to see if the bias column should be added
        if addBias:
            # insert a column of 1's as the last entry in the feature
            # matrix (bias)
            X = np.c_[X, np.ones((X.shape[0]))]

        # take the dot product between the input features and the
        # weight matrix, then pass the value through the step
        # function
        return self.step(np.dot(X, self.W))