#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# convert the image from the RGB colorspace to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

"""
cv2.calcHist(images, channels, mask, histSize, ranges)
    images: Wrap it as a list [myImage]
    channels: the index of the channel
    mask: If a mask is provided, a histogram will be computed for masked pixels only
    histSize: the number of bins
    ranges: specify the range of possible pixel values
"""
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
# plt.plot() plots grayscale histogram
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
