#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# import the necessary packages
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder          # helper utility to convert labels represented as strings to integers
from sklearn.model_selection import train_test_split    # help us create our training and testing splits
from sklearn.metrics import classification_report       # help us evaluate the performance of our classifier and print a nicely formated table of result.
from preprocessing.simplepreprocessor import SimplePreprocessor
from datasets.simpledatasetloader import SimpleDatasetLoader
from imutils import paths
import argparse


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="path to input dataset")
ap.add_argument("-k", "--neighbors", type=int, default=1,
                help="# of nerest neighbors for classification")
# Optional, the number of concurrent jobs to run when computing the distance between an input data point and the training set.
# A value of -1 will use all available cores on the processor.
ap.add_argument("-j", "--jobs", type=int, default=-1,
                help="# of jobs for k-NN distance (-1 uses all available cores)")
args = vars(ap.parse_args())

#---------------------------------
# Step#1
#---------------------------------

# grab the list of images that we'll be describing
print("[INFO] loading images...")
imagePaths = list(paths.list_images(args["dataset"]))
#print('imagePaths len %s' %len(imagePaths))

# initialize the image preprocessor, load the dataset from disk,
# and reshape the data matrix
sp = SimplePreprocessor(32,32)
sdl = SimpleDatasetLoader(preprocessors=[sp])
(data, labels) = sdl.load(imagePaths, verbose=500)
data = data.reshape(data.shape[0], 3072) # falttening the 32 x 32 x 3 images into an array with shape (3072)

# show some information on memeory consymption of the image
print("[INFO] features matrix: {:.1f}MB".format(data.nbytes / (1024 * 1000.0)))

#----------------------------------
# Step#2
#----------------------------------
#encode the labels as integers
# many machine learning algrithms assume that the class labels are encoded as integers
le = LabelEncoder()
labels = le.fit_transform(labels)

# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
(trainX, testX, trainY, testY) = train_test_split(data, labels,
                                                 test_size=0.25, random_state=42)

#----------------------------------
# Step#3
#----------------------------------
# train and evaluate a k-NN classifier on the raw pixel intensities
print("[INFO] evaluating k-NN classifer...")
model = KNeighborsClassifier(n_neighbors=args["neighbors"],
                             n_jobs=args["jobs"])
# trains the classifier
model.fit(trainX, trainY)
# evaluate our classifier
print(classification_report(testY, model.predict(testX),
                            target_names=le.classes_))


"""
    Using:
        python3 k-NN.py --dataset ../datasets/animals
    
    Pros and Cons of k-NN 
        1. k-NN algrothm is extrmely simple to implement and understand.
    
    Drawback:
        1. it doesn't actually "learn" anything - if the algorithm makes a mistake, it has no way to "correct" and "improve" itself for later classifications.
        2. without specialized data structures, the k-NN algorithm scales linearly with the number of data points, making it not only practically challenging to use in high dimensions.
"""