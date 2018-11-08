#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import cv2
# OpenCV actually stores the pixel values in Blue, Green, Red order

image = cv2.imread("../datasets/SteveJobsOneMoreThing.jpg")
print(image.shape)
print(image[20,100]) # access values in a matrix: first we specify the row number then the column number
cv2.imshow("datasets/SteveJobsOneMoreThing.jpg", image)
cv2.waitKey(0)