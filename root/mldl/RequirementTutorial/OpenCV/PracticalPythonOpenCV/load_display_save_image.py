#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
args = vars(ap.parse_args())


# returns a NumPy array representing the image
image = cv2.imread(args["image"])
#import pdb; pdb.set_trace()  # XXX BREAKPOINT
# Numpy shape height width channels
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))


# handle displaying the actual image on our screen
cv2.imshow("Image", image)
# pause the execution of the script until press a key, 0 indicates that any keypress
cv2.waitKey(0)

cv2.imwrite("{}/newimage.jpg".format(''.join(args['image'].split('/')[:-1])), image)
