#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
import argparse
import mahotas
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

T = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold: {}".format(T))

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)
cv2.waitKey(0)

ret, th = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("Otsu's threshold: {}".format(ret))

thresh = image.copy()
thresh[thresh > ret] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)
cv2.waitKey(0)

#rc: Riddler-Calvard method
T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)
