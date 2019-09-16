#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
This file will store basic image processing methods, allowing us to conveniently call them without writting a lot of code.
"""
import numpy as np
import cv2


def translate(image, x, y):
    """
    @param image: the image
    @param x: shift along the x-axis
    @param y: shift along the y-axis
    """
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted


def rotate(image, angle, center = None, scale = 1.0):
    """
    @param image:
    @param angle: angle Θ
    @param center: which point rotate around
    @param scale:
    """
    (h, w) = image.shape[:2]
    if center is None:
        center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated


def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    """
    @param image:
    @param width:
    @param height:
    @param inter:
    """
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)
    return resized
