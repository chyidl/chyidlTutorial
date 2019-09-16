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

# grabs the width and height of the image. Integer division is used here "//"
(h, w) = image.shape[:2]
# "//" to ensure we receive whole integer numbers
center = (w // 2, h // 2)

"""
cv2.getRotationMatrix2D
    the first argument: which image
    the second argument: degrees
    the thrid argument: the scale of the image
"""
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degress", rotated)

rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)
