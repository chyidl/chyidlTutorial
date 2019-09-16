#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import argparse  # argparse to handle parsing our command line arguments.
import cv2  # OpenCV library


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
# parse the arguments and store them in dictionary
args = vars(ap.parse_args())


# cv2.imread function returns a NumPy array representing the image
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

# write image to file in JPEG format.
cv2.imwrite("{}/newimage.jpg".format(''.join(args['image'].split('/')[:-1])), image)
