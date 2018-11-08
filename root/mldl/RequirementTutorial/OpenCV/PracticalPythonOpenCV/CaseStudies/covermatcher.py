#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
import cv2


class CoverMatcher:
    def __init__(self, descriptor, coverPaths, ratio = 0.7,
        minMatches = 40, useHamming = True):
        self.descriptor = descriptor
        self.coverPaths = coverPaths
        self.ratio = ratio
        self.minMatches = minMatches
        self.distanceMethod = "BruteForce"

        if useHamming:
            self.distanceMethod += "-Hamming"

    def search(self, queryKps, queryDescs):
        results = {}

        for coverPath in self.coverPaths:
            cover = cv2.imread(coverPath)
            gray = cv2.cvtColor(cover, cv2.COLOR_BGR2GRAY)
            (kps, descs) = self.descriptor.describe(gray)

            score = self.match(queryKps, queryDescs, kps, descs)
            results[coverPath] = score

        if len(results) > 0:
            results = sorted([(v, k) for (k, v) in results.items() if v > 0],
                        reverse = True)
        return results

    def match(self, kpsA, featuresA, kpsB, featuresB):
        matcher = cv2.DescriptorMatcher_create(self.distanceMethod)
        rawMatches = matcher.knnMatch(featuresB, featuresA, 2)
        matches = []

        for m in rawMatches:
            if len(m) == 2 and m[0].distance < m[1].distance * self.ratio:
                matches.append((m[0].trainIdx, m[0].queryIdx))

        if len(matches) > self.minMatches:
            ptsA = np.float32([kpsA[i] for (i, _) in matches])
            ptsB = np.float32([kpsB[j] for (_, j) in matches])
            (_, status) = cv2.findHomography(ptsA, ptsB, cv2.RAWSAC, 4.0)
            return float(status.sum()) / status.size

        return -1.0
