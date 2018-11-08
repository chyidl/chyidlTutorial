#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from rgbhistogram import RGBHistogram
# [sunflowers向日葵, crocus番红花, daisies雏菊, pansies三色青, ]
from sklearn.preprocessing import LabelEncoder # distinguish between flower species
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split # training set, testing set
from sklearn.metrics import classification_report
import numpy as np
import argparse
import glob # glob the paths of images off disk
import cv2
import imutils

ap = argparse.ArgumentParser()
# The images used in this example are a sample of the Flowers 17 dataset
# http://www.robots.ox.ac.uk/~vgg/data/flowers/17/index.html
ap.add_argument("-i", "--images", required = True,
    help = "path to the image dataset")
ap.add_argument("-m", "--masks", required = True,
    help = "path to the image masks")
args = vars(ap.parse_args())

imagePaths = sorted(glob.glob(args["images"] + "/*.jpg"))
maskPaths = sorted(glob.glob(args["masks"] + "/*.png"))

data = []
target = []

desc = RGBHistogram([8, 8, 8])

for (imagePath, maskPath) in zip(imagePaths, maskPaths):
    image = cv2.imread(imagePath)
    mask = cv2.imread(maskPath)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    features = desc.describe(image, mask)

    data.append(features)
    target.append(imagePath.split("_")[-2])

targetNames = np.unique(target)
le = LabelEncoder()
target = le.fit_transform(target)

(trainData, testData, trainTarget, testTarget) = train_test_split(data, target,
                                                test_size = 0.3, random_state = 42)

# using 25 decision trees in the forest
model = RandomForestClassifier(n_estimators = 25, random_state = 84)
model.fit(trainData, trainTarget)

# classification_report function print out the accuracy of his model
print(classification_report(testTarget, model.predict(testData),
    target_names = targetNames))

# randomly picks 10 different images to in-vestigate
for i in np.random.choice(np.arange(0, len(imagePaths)), 10):
    imagePath = imagePaths[i]
    maskPath = maskPaths[i]

    image = cv2.imread(imagePath)
    mask = cv2.imread(maskPath)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    features = desc.describe(image, mask)

    flower = le.inverse_transform(model.predict([features]))[0]
    print(imagePath)
    print("I think this flower is a {}".format(flower.upper()))
    cv2.imshow("image", image)
    cv2.waitKey(0)
