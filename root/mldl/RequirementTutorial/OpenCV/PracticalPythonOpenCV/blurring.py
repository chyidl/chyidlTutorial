#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# The first blurring method : Averaging
# define a k x k sliding window, where k is alway an odd number.
# the center of this marix set to be the average of all other pixels surrounding it.
# hstack: horizontally stacks
blurred = np.hstack([
    # blur function
    cv2.blur(image, (3, 3)),
    cv2.blur(image, (5, 5)),
    cv2.blur(image, (7, 7))])
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)

# The second blurring method : Gaussian
# weighted mean, where neighborhood pixels that are closer to the central pixel
blurred = np.hstack([
    # The last parameer is our σ
    cv2.GaussianBlur(image, (3, 3), 0),
    cv2.GaussianBlur(image, (5, 5), 0),
    cv2.GaussianBlur(image, (7, 7), 0)])

cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)

# The Third blurring method : Median
# Using the median blur method, can remove the salt and pepper from image
blurred = np.hstack([
    # replace the central pixel with the median of the neighborhood
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7)])

cv2.imshow("Median", blurred)
cv2.waitKey(0)

# The Fouth Method : bilateral bluring
# reduce noise while still maintaining edges
blurred = np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21),
    cv2.bilateralFilter(image, 7, 31, 31),
    cv2.bilateralFilter(image, 9, 41, 41)])
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)
