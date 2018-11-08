#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 清洗数据
import os
import glob
import argparse

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

imagePathsPrefix = list(map(lambda x: x.split('/')[-1][:-4], imagePaths))
maskPathsPrefix = list(map(lambda x: x.split('/')[-1][:-4], maskPaths))

subPaths = list(set(imagePathsPrefix) - set(maskPathsPrefix))
prepareDelete = list(map(lambda x: '/'.join(imagePaths[0].split('/')[:-1])+'/'+x+'.jpg',subPaths))

for file in prepareDelete:
    os.remove(file)
    print("delete file {}".format(file))


