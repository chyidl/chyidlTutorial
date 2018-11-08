#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# import the necessary package
import cv2


# load a image from disk and resized it to a fixed, ugnoring aspect ratio.
class SimplePreprocessor:
    def __init__(self, width, height, inter=cv2.INTER_AREA):
        """
        :param width: # The target width of our image after resizing
        :param height: # The target height of our input image after resizing
        :param inter: # An optional parameter used to control which interpolation algorithm is used when resizing
        """
        # store the target image width, height, and interpolation
        # method used when resizing
        self.width = width
        self.height = height
        self.inter = inter


    def preprocess(self, image):
        # resize the image to a fixed size, ignoring the aspect
        # ratio
        return cv2.resize(image, (self.width, self.height), interpolation=self.inter)