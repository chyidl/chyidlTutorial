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
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Applying Gaussian blurring helps remove some of the high frequency edges in the image
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

# compute the thresholded image
# THRESH_BINARY method, which indicates that pixel values p greater than T are
# set to the maximum value
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binrary", thresh)

# THRESH_BINARY_INV inverse thresholding
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

# reveal image and hide everything
cv2.imshow("Apple", cv2.bitwise_and(image, image, mask = threshInv))
cv2.waitKey(0)
