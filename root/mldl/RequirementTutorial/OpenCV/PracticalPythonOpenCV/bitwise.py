#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Bitwise operations operate in a binary manner and are represented as grayscale
# images.
# A given pixel is turned "off" if it has a value of zero, and it is turned
# "on" if the pixel has a value greater than zero
"""
bitwise operation:
    AND : A bitwise AND is true if and only if both pixels are greater than zero
    OR  : A bitwise OR is true if either of the two pixels are greater than zero
    XOR : A bitwise XOR is true if and only if either of the two pixels are greater than zero, but not both
    NOT : A bitwise NOT inverts the "on" and "off" pixels in an image.
"""
import numpy as np
import cv2

# Initialize our rectangle image
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

# initialize circle
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)
