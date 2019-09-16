#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help = "Path to the image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
cv2.imshow("Original", image)


# OpenCV stores RGB channels in reverse order, OpenCV actually stores them in the order of Blue, Green, and Red
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))


# Start y End y, Start x End x
corner = image[0: 100, 0:100]
cv2.imshow("Corner", corner)


image[0: 100, 0:100] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)
