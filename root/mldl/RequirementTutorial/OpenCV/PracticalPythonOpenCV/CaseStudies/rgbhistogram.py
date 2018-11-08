#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import cv2


class RGBHistogram:
    def __init__(self, bins):
        self.bins = bins

    def describe(self, image, mask = None):
        hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins, [0, 256, 0, 256, 0, 256])
        cv2.normalize(hist, hist)

        return hist.flatten()
