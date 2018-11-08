#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import imutils
import numpy as np
import cv2
import mahotas


def load_digits(datasetPath):
    # genfromtext function of NumPy loads the dataset off disk and stores it
    data = np.genfromtxt(datasetPath, delimiter = ",", dtype = "uint8")
    target = data[:, 0] # The target will fall into the range [0, 9]
    data = data[:, 1:].reshape(data.shape[0], 28, 28)

    return (data, target)


# The first is the image of the digit that is going to be deskwed
# The second is the width that the image is going to be resized to
def deskew(image, width):
    (h, w) = image.shape[:2]
    moments = cv2.moments(image)

    skew = moments["mu11"] / moments["mu02"]
    M = np.float32([
        [1, skew, -0.5 * w * skew],
        [0, 1, 0]])
    # The actual deskewing of the image take places
    image = cv2.warpAffine(image, M, (w, h),
        flags = cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)

    image = imutils.resize(image, width = width)

    return image

def center_extent(image, size):
    (eW, eH) = size

    if image.shape[1] > image.shape[0]:
        image = imutils.resize(image, width = eW)
    else:
        image = imutils.resize(image, height = eH)

    extent = np.zeros((eH, eW), dtype = "uint8")
    offsetX = (eW - image.shape[1]) // 2
    offsetY = (eH - image.shape[0]) // 2
    extent[offsetY:offsetY + image.shape[0], offsetX:offsetX + image.shape[1]] = image

    CM = mahotas.center_of_mass(extent)
    (cY, cX) = np.round(CM).astype("int32")
    (dX, dY) = ((size[0] // 2) - cX, (size[1] // 2) - cY)
    M = np.float32([[1, 0, dX], [0, 1, dY]])
    extent = cv2.warpAffine(extent, M, size)

    return extent
