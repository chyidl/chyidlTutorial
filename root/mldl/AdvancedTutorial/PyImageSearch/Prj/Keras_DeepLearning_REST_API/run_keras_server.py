#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# run_keras_server.py
# Keras_DeepLearning_REST_API
#
# 🎂"Here's to the crazy ones. The misfits. The rebels.
# The troublemakers. The round pegs in the square holes.
# The ones who see things differently. They're not found
# of rules. And they have no respect for the status quo.
# You can quote them, disagree with them, glority or vilify
# them. About the only thing you can't do is ignore them.
# Because they change things. They push the human race forward.
# And while some may see them as the creazy ones, we see genius.
# Because the poeple who are crazy enough to think thay can change
# the world, are the ones who do."
#
# Created by Chyi Yaqing on 08/12/18 13:48.
# Copyright © 2018. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT

"""
%HERE%
"""
# import the necessary packages
from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from threading import Thread
from PIL import Image
import numpy as np
import base64
import flask    # Flask library Used to build our Web API
import redis    # module enable us to interface with the Redis data store
import uuid
import json
import sys
import io


# Initialize constant used to control image spatial dimensions and data type
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
IMAGE_CHANS = 3
IMAGE_DTYPE = "float32"

# initialize constants used for server queuing
IMAGE_QUEUE = "image_queue"
BATCH_SIZE = 32
SERVER_SLEEP = 0.25
CLIENT_SLEEP = 0.25

# initialize our Flask application, Redis server, and Keras model
app = flask.Flask(__name__)
# the default host and port values for Redis
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
db = redis.StrictRedis(connection_pool=pool)
# initialize a global Keras model to None
model = None

# handle serialization of images
def base64_encode_image(a):
    # base64 encode the input NumPy array
    return base64.b64encode(a).decode("utf-8")

def base64_decode_image(a, dtype, shape):
    # if this is Python 3, we need the extra step of encoding the
    # serialized Numpy string as a byte object
    if sys.version_info.major == 3:
        a = bytes(a, encoding="utf-8")

    # convert the string to a NumPy array using the supplied data
    # type and target shape
    a = np.frombuffer(base64.decodestring(a), dtype=dtype)
    a = a.reshape(shape)

    # return the decoded image
    return a

# Redis will act as our temporart data store on the server. Images will comes
# in to the server via a variety of methods such as cURL, a Python script, or
# even a mobile app.

# In order to store our images in Redis, they need to be serialized. Since
# images are just NumPy arrays, we can utilize base64 encoding to serialize the
# images. Using base64 encoding also has the added benefit of allowing us to
# use JSON to store additional attributes with the image.

# pre-process our image
def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image

# define classification method
def classify_process():
    # load the pre-trained Keras model (here we are using a model
    # pre-trained on ImageNet and provided by Keras, but you can
    # substitute in your own networks just as easily)
    print("* Loading model...")
    model = ResNet50(weights="imagenet")
    print("* Model loaded")

