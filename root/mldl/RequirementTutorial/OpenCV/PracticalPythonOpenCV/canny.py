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
# remove "noisy" edges in the image
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", image)

# Values in between threshold1 and threshold2 are either classified as edges
# or non-edges based on how their intensities
canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
