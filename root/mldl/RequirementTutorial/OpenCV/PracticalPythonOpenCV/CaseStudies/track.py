#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
import argparse
import cv2
import time
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help = "path to the (optional) video file")
args = vars(ap.parse_args())

# shades of blue
blueLower = np.array([100, 67,0], dtype = "uint8")
blueUpper = np.array([255, 128, 50], dtype = "uint8")

if not args.get("video", False):
    # VideoCapture value 0 instructs OpenCV to read the webcam device
    camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])

while True:
    (grabbed, frame) = camera.read()
    if not grabbed:
        break

    frame = imutils.resize(frame, width = 300)

    # find shades of blue in the frame
    blue = cv2.inRange(frame, blueLower, blueUpper)
    # pixels falling within the upper and lower range set to white and pixel
    # do not fall into this range set as black
    blue = cv2.GaussianBlur(blue, (3,3), 0)

    # find the con-tours
    (_, cnts, _) = cv2.findContours(blue.copy(),
                                    cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) > 0:
        # cv2.contourArea function to compute the area of the contour
        cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)

    cv2.imshow("Tracking", frame)
    cv2.imshow("Binary", blue)

    time.sleep(0.025)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()
