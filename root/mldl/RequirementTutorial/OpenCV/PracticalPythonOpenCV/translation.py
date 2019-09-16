#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
import argparse
import imutils
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Translation matrix M. This matrix how many pixels to the left or right, and up or down, the image will be shifted
# [1, 0, tx] shift the image left or right, tx Negative shift left; positive right
# [0, 1, ty] shift the image up or down, Negative ty shift up and positive shift down
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)


M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
