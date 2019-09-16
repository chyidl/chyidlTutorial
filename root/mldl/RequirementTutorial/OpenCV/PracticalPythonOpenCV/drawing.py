#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
We can define our images manually using NumPy arrays, Given that
OpenCV interprets an image as a NumPy arrays.
"""
import numpy as np
import cv2


# construct a NumPy array using the np.zeros method
# canvas initialized.
canvas = np.zeros((300, 300, 3), dtype="uint8")


green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


red = (0, 0, 255)
# the thickness
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# the thickness: 5 pixels
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# the thickness: negative value "filled in"
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# re-initialize canvas to be blank
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    # r is the radius of the circle
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw 25 random circles
for i in range(0, 25):
    # radius of the circle
    radius = np.random.randint(5, high = 200)
    # the color of the circle
    color = np.random.randint(0, high = 256, size = (3,)).tolist()
    # the pt - the (x,y) coordinate of where the circle will be drawn
    pt = np.random.randint(0, high = 300, size = (2,))
    # use a thickness of -1
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
