#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# import the necessary package
import numpy as np
import cv2
import os


# using this class to load small image datasets from disk
class SimpleDatasetLoader:
    def __init__(self, preprocessors=None):
        """
        :param preprocessors: as list rather than a single value
        """
        # store the image preprocessor
        self.preprocessors = preprocessors

        # if the preprocessors are None, initialize them as a
        # empty list
        if self.preprocessors is None:
            self.preprocessors = []

    def load(self, imagePaths, verbose=-1):
        """
        :param imagePaths: which is a list specifying the file paths to the images in our dataset residing on disk.
        :param verbose: print updates to a console
        :return:
        """
        # initialize the list of features and labels
        data = []
        labels = []

        # loop over the input images
        for (i, imagePath) in enumerate(imagePaths):
            # Load the image and extract the class label assuming
            # that our path has the following format:
            # /path/to/dataset/{class}/{image}.jpg
            image = cv2.imread(imagePath)
            label = imagePath.split(os.path.sep)[-2]
            # check to see if our preprocessors are not None
            if self.preprocessors is not None:
                # loop over the preprocessors and apply each to
                # the image
                for p in self.preprocessors:
                    image = p.preprocess(image)

            # treat our processed image as a "feature vector"
            # by updating the data list followed by the labels
            data.append(image)
            labels.append(label)

            # show an update every 'verbose' image
            if verbose > 0 and i > 0 and (i + 1) % verbose == 0:
                print("[INFO] processed {}/{}".format(i + 1, imagePath.split('/')[-1]))

        # return a tuple of the data and labels
        return (np.array(data), np.array(labels))