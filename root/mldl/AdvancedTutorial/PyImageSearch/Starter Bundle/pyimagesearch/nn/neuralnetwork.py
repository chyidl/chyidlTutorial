#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Implementing Backpropagation with Python
# import the necessary packages
import numpy as np


class NeuralNetwork:
    def __init__(self, layers, alpha=0.1):
        """
        :param layers:  A list of integers which represents the actual architecture of the feedforward.
        :param alpha:   specify the learning rate of our neural network
        """
        # initialize the list of weights matrices, then store the
        # network architecture and learning rate
        self.W = []
        self.layers = layers
        self.alpha = alpha

        # start looping from the index of the first layer but
        # stop before we reach the last two layers
        for i in np.arange(0, len(layers) - 2):
            # randomly initialize a weight matrix connecting the
            # adding an extra node for the bias
            # adding an extra node for the bias
            # The matrix is MxN since we wish to connect every node in current layer to every node in the next layer
            w = np.random.randn(layers[i] + 1, layers[i + 1] + 1)
            self.W.append(w / np.sqrt(layers[i])) # Thereby normalizing the variance

        # the last two layers are a special case where the input
        # connections need a bias term but the output does not
        w = np.random.randn(layers[-2] + 1, layers[-1])
        self.W.append(w / np.sqrt(layers[-2]))

    # this function is useful for debugging
    def __repr__(self):
        # construct and return a string theta represents the network
        # architecture
        return "NeuralNetwork: {}".format("-".join(str(l) for l in self.layers))

    # activation function
    def sigmoid(self, x):
        # compute and return the sigmoid activation value for a
        # given input value
        return 1.0 / (1 + np.exp(-x))

    # derivative of the sigmoid
    def sigmoid_deriv(self, x):
        # compute the derivative of the sigmoid function ASSUMING
        # that 'x' has already been passed through the 'sigmoid'
        # function
        return x * (1 - x)

    def fit(self, X, y, epochs=1000, displayUpdate=100):
        """
        :param X: training data
        :param y: corresponding class labels
        :param epochs: which is the number of epochs we'll train our network for
        :param displayUpdate: how many N epochs we'll print training progress to our terminal
        :return:
        """
        # insert a column of 1's as the last entry in the feature
        # matrix -- this little trick allows us to treat the bias
        # as a trainable parameter within the weight matrix
        X = np.c_[X, np.ones((X.shape[0]))]

        # loop over the desired number of epochs
        for epoch in np.arange(0, epochs):
            # loop over each individual data point and train
            # our network on it
            for (x, target) in zip(X, y):
                # The actual heart of the backpropagation algorithm is found
                self.fit_partial(x, target)

            # check to see if we should display a training update
            if epoch == 0 or (epoch + 1) % displayUpdate == 0:
                loss = self.calculate_loss(X, y)
                print("[INFO] epoch={}, loss={:.7f}".format(epoch + 1, loss))

    # The backpropagation algorithm is found inside our fit_partial
    def fit_partial(self, x, y):
        """
        :param x: An individual data point from our design matrix
        :param y: The corresponding class label
        :return:
        """
        # construct our list of output activations for each layer
        # as our data point flows through the network; the first
        # activation is a special case -- it's just the input
        # feature vector itself
        A = [np.atleast_2d(x)] # View inputs as arrays with at least two dimensions

        # FEEDFORWARD
        # loop over the layers in the network
        for layer in np.arange(0, len(self.W)):
            # feedforward the activation at the current layer by
            # taking the dot product between the activation and
            # the weight matrix -- this is called the "net input"
            # to the current layer
            # taking the dot product between the activation and the weights.
            net = A[layer].dot(self.W[layer])

            # computing the "net output" is simply applying our
            # nonlinear activating function to the net input
            out = self.sigmoid(net)

            # once we have the net output, add it to our list of
            # activations
            A.append(out)

        # BACKPROGATION
        # the first phase of backpropagation is to compute the
        # difference between our *prediction* (the final output
        # activation in the activations list) and the true target
        # value
        error = A[-1] - y  # different between our predicted label and the ground-truth label

        # from here, we need to apply the chain rule and build our
        # list of deltas 'D; the first entry in the deltas is
        # simply the error of the output layer times the derivative
        # of our activation function for the output value
        D = [error * self.sigmoid_deriv(A[-1])] # The deltas will be used to update our weight matrices, scaled by the learning rate alpha

        # Work backward
        # once you understand the chain rule it becomes super easy
        # to implement with a 'for' loop -- simply loop over the
        # layers in reverse order (ignoring the last two since we
        # already have taken them into account)
        for layer in np.arange(len(A) -2, 0, -1):
            # the delta for the current layer is equal to the delta
            # of the *previous layer* dotted with the weight matrix
            # of the current layer, followed by multiplying the delta
            # by the derivative of the nonlinear activation function
            # for the activations of the current layer
            delta = D[-1].dot(self.W[layer].T)
            delta = delta * self.sigmoid_deriv(A[layer])
            D.append(delta)

        # since we looped over our layers in reverse order we need to
        # reverse the deltas
        D = D[::-1]

        # WEIGHT UPDATE PHASE
        # loop over the layers
        for layer in np.arange(0, len(self.W)):
            # update our weights by taking the dot product of the layer
            # activations with their respective deltas, then multiplying
            # this value by some small learning rate and adding to our
            # weight matrix -- this is where the actual "learning" takes
            # place
            self.W[layer] += -self.alpha * A[layer].T.dot(D[layer])

    def predict(self, X, addBias=True):
        """
        :param X: The data points we'll be predicting class labels for
        :param addBias: A boolean indicating whether we need to add a column of 1's to X to perform the bias trick
        :return:
        """
        # initialize the output prediction as the input features -- this
        # value will be (forward) propagated through the network to
        # obtain the final prediction
        p = np.atleast_2d(X)

        # check to see if the bias column should be added
        if addBias:
            # insert a column of 1's as the last entry in the feature
            # matrix (bias)
            p = np.c_[p, np.ones((p.shape[0]))] # Translates slice objects to concatenation along the second axis

        # loop over our layers in the network
        for layer in np.arange(0, len(self.W)):
            # computing the output prediction is as simple as taking
            # the dot product between the current activation value 'p'
            # and the weight matrix associated with the current layer
            # then passing this value through a nonlinear activation
            # function
            p = self.sigmoid(np.dot(p, self.W[layer]))

        # return the predicted value
        return p

    # calculate the loss across our entire training set
    def calculate_loss(self, X, targets):
        # make predictions for the input data points then compute
        # the loss
        targets = np.atleast_2d(targets)
        predictions = self.predict(X, addBias=False)
        loss = 0.5 * np.sum((predictions - targets) ** 2)

        # return the loss
        return loss





if __name__ == '__main__':
    nn = NeuralNetwork([2, 2, 1])
    print(nn)

"""
    te
"""