#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# flip code 1 indicates horizontally, around the y-axis
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# flip code 0 indicates vertically, around the x-axis
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# negative flip code -1 flip the image around both axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)
