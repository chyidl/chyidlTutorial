#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import argparse  # argparse to handle parsing our command line arguments.
import cv2  # OpenCV library
from matplotlib import pyplot as plt


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
# parse the arguments and store them in dictionary
args = vars(ap.parse_args())


# cv2.imread function returns a NumPy array representing the image
"""
cv2.imread(param1, param2)
    param1: full path of image
    param2: which specifies the way image should be read.
        cv2.IMREAD_COLOR: load a color image. -- it is the default flag 1
        cv2.IMREAD_GRAYSCALE: loads image in grayscale mode 0
        cv2.IMREAD_UNCHANGED: loads image as such including alpha channel -1
"""
image = cv2.imread(args["image"], 1)
#import pdb; pdb.set_trace()  # XXX BREAKPOINT
# Numpy shape height width channels
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))


# handle displaying the actual image on our screen
cv2.imshow("Image", image)
# pause the execution of the script until press a key, 0 indicates that any keypress
cv2.waitKey(0)
# destroys all the window we created
cv2.destroyAllWindows()
# destroy any specific window
#cv2.destroyWindow()

# cv2.WINDOW_AUTOSIZE, cv2.WINDOW_NORMAL
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread(args["image"], 0)
cv2.imshow('image', image)
k = cv2.waitKey(0) & 0xFF
if k == 27:  # wait for Esc key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' ket to save and exit
    # write image to file in JPEG format.
    cv2.imwrite("{}/newimage.jpg".format(''.join(args['image'].split('/')[:-1])), image)
    cv2.destroyAllWindows()

image = cv2.imread(args["image"], 0)
plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
