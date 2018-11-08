# TensorFlow Object Detection on the Raspberry Pi 

## About 

This is a guide on how to setup tensorflow object detection API on Raspberry pi. will be use pre-trained Object detection neural network to detect and identify object in a Live Pi camera video.

Tensorflow version: 1.11.0 

Raspberry Pi Details:
  Type: Pi 3, Revision: 02, Memory: 1024MB, Maker: Sony 
  * Device tree is enabled.
  *--> Raspberry Pi 3 Model B Rev 1.2

$ lsb_release -a
No LSB modules are available.
Distributor ID:	Raspbian
Description:	Raspbian GNU/Linux 9.4 (stretch)
Release:	9.4
Codename:	stretch

## Update the Raspberry Pi 

**the Raspberry Pi needs to be fully update**

```
$ sudo apt-get update 
$ sudo apt-get upgrade -y 
$ sudo apt-get dist-upgrade  
```

## Install TensorFlow 

```
$ wget https://github.com/lhelontra/tensorflow-on-arm/releases/download/v1.11.0/tensorflow-1.11.0-cp35-none-linux_armv7l.whl
$ sudo pip3 install tensorflow-1.11.0-cp35-none-linux_armv7l.whl

# Tensorflow need the LibAtlas package. 
$ sudo apt-get install libatlas-base-dev

# install other dependencies that will be used by TensorFlow Object Detection API 
$ sudo pip3 install pillow lxml jupter matplotlib cython 
$ sudo apt-get install python3-tk 

```

## Install OpenCV 

## Compile and Install Protobuf 

Tensorflow object detection API uses Protobuf, a package that implements Google's Protocol Buffer data format. 

```
# First, get the packages needed to compile Protobuf from source. 
$ sudo apt-get install autoconf automake libtool curl 

# Then download the protobuf release from its Github repository 
$ wget https://github.com/protocolbuffers/protobuf/releases/download/v3.6.1/protobuf-all-3.6.1.tar.gz

# Unpack the file and cd into the folder 
$ tar -zxvf protobuf-all-3.6.1.tar.gz 
$ cd protobuf-3.6.1 
$ ./configure 
$ make -j4 && make check 
$ sudo make install 

# Then move into the Python directory and export the library path:
$ cd python
$ export LD_LIBRARY_PATH=../src/.libs 

# 
$ python3 setup.py build --cpp_implementation 
$ python3 setup.py test --cpp_implementation 
$ sudo python3 setup.py install --cpp_implementation 

# 
$ export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp 
$ export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION_VERSION=3

#
$ sudo ldconfig 

# That's it! Now Protobuf is installed on the Pi. Verify it's installed correctly by issuing the command below and making sure it puts out the default help text. 
$ protoc 

# For some reason. the Raspberry pi needs to be restarted after this process, or TensorFlow will not work. Go ahead and reboot the Pi by issuing 
$ sudo reboot now 
```

## Set up TensorFlow Directory Structure and PYTHONPATH Variable 

```
$ mkdir tensorflow 
$ cd tensorflow 

# Download the tensorflow repository from GitHub 
$ git clone --recurse-submodules https://github.com/tensorflow/models.git 

```

