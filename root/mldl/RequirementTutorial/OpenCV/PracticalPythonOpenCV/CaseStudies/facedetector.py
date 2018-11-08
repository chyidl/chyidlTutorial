#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import cv2


# use the OpenCV built-in Haar cascade classifiers
# Haar cascade classifiers have already been pre-trained to recognize faces
#
# Building own classifier need a lot of "positive" and "negative" images
# "Positive" images would contain images with faces
# "negative" images would contain image without faces
class FaceDetector:
    def __init__(self, faceCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

    def detect(self, image, scaleFactor = 1.1, minNeighbors = 5,
        minSize = (30, 30)):
        # detectMultiScale method returns rects, a list of tuple containing the
        # bounding boxes of the faces in the image
        rects = self.faceCascade.detectMultiScale(image,
            scaleFactor = scaleFactor,
            minNeighbors = minNeighbors, minSize = minSize,
            flags = cv2.CASCADE_SCALE_IMAGE)

        return rects
