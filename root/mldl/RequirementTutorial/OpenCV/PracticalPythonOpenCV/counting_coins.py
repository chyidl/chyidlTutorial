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
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (15, 15), 0)
cv2.imshow("Image", image)

edged = cv2.Canny(blurred, 50, 100)
cv2.imshow("Edges", edged)

"""
cv2.findContours
    the first param: edged image
    the second param: the type of contours (
        cv2.RETR_EXTERNAL: retrieve only the outermost contours;
        cv2.RETR_LIST: grab all contours
        cv2.RETR_COMP、cv2.RETR_TREE
    )
    the thrid param: cv2.CHAIN_APPROX_SIMPLE
"""
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("I count {} coins in this image".format(len(cnts)))

coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)

# Crop each individual coin from the image
for (i, c) in enumerate(cnts):
    # boundingRect function finds the "enclosing box" that contour will fit into
    (x, y, w, h) = cv2.boundingRect(c)

    print("Coin #{}".format(i + 1))
    coin = image[y:y + h, x: x + w]
    cv2.imshow("Coin", coin)

    mask = np.zeros(image.shape[:2], dtype = "uint8")
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius),
        255, -1)
    mask = mask[y:y + h, x:x + w]
    cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))
    cv2.waitKey(0)
