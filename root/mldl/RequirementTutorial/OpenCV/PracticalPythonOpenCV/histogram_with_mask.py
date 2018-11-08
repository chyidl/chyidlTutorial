#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2


def plot_histogram(image, title, mask = None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    for (chan, color) in zip(chans, colors):
        # computes a histogram for each channel in the image and plots it
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color = color)
        plt.xlim([0, 256])


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
plot_histogram(image, "Histogram for Original Image")

# Construct a mask
height, width = image.shape[:2]
mask = np.zeros((height, width), dtype = "uint8")
# draw a white rectangle
cv2.rectangle(mask, (height // 2 - 50, width // 2 - 50), (height // 2 + 50, width // 2 + 50), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Applying the Mask", masked)

# compute a histogram for our masked image
plot_histogram(image, "Histogram for Masked Image", mask = mask)

plt.show()
