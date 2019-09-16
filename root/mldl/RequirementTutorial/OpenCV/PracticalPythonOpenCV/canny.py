#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Canny Edge Detection is a popular edge detection algorithm. It was developed by John F.Canny in 1986. It is a multi-stage algorithm algorithm and we will go through each stages.
    1. Noise Reduction
        Since edge detection is susceptible to noise in the image, first step is to remove the noise in the image with a 5 x 5 Gaussian filter.
    2. Finding Intensity Gradient of the image
        Gradient direction is always perpendicular to edges. it is rounded to one of four angles representing vertical, horizontal and two diagonal directions.
    3. Non-maximum Suppression:
        After getting gradient magnitude and direction, a full scan of image is done to remove any unwanted pixels which may not constitude the edge.
    4.
"""
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
