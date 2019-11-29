Smart Security Camera
=====================
> IoT security camera running open-cv for object detection. The camera will send an email with an image of any objects it detects. It also runs a server that provides a live video stream over the internet.

* Stepup
```
This project uses a Raspberry Pi Camera to stream video. make sure to configure the raspberry pi camera on your device.
$ sudo raspi-config 
Select Interface Options, then Pi Camera and toggle on. Press Finish and exit.

You can verify that the camera works by running 
$ raspistill -rot 180 -o image.jpg
Which will save a image from the camera in your current directory. You can open up the file inspector and view the image.
```

* Install OpenCV 4 on Raspberry Pi 3B and Raspbian Buster
```
Step #1: Expand filesystem and reclaim space 
$ sudo raspi-config 
select the 7 Advanced Options 
select the A1 Expand filesystem

Step #2: Install dependencies 
# The first step is to update and upgrade any existing packages:
$ sudo apt-get update && sudo apt-get upgrade 

# install developer tools, including CMake 
$ sudo apt-get install build-essential cmake pkg-config 

# install image I/O packages that allow to load various image file formats from disk
$ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev

# install vidoe I/O package that allow to read various video file formats from disk as well as work directly with vide streams 
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
$ sudo apt-get install libxvidcore-dev libx264-dev

# install the GTK development library and prerequistes
$ sudo apt-get install libfontconfig1-dev libcairo2-dev
$ sudo apt-get install libgdk-pixbuf2.0-dev libpango1.0-dev
$ sudo apt-get install libgtk2.0-dev libgtk-3-dev

# optimized OpenCV matrix operations 
$ sudo apt-get install libatlas-base-dev gfortran

# HDF5 datasets  and Qt GUIs 
$ sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103
$ sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5

# install python 3 headers files
$ sudo apt-get install python3-dev

Step #3: Create Python virtual environment and install Numpy 
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py
$ sudo rm -rf ~/.cache/pip

# install virtualenv and virtualenwrapper
$ sudo pip install virtualenv virtualenvwrapper
$ vim ~/.zshrc 
# append the following lines to the bottom of the file
    # virtualenv and virtualenvwrapper
    export WORKON_HOME=$HOME/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    source /usr/local/bin/virtualenvwrapper.sh

# reload ~/.zshrc file to apply the changes to your current bash sessions
$ source ~/.bashrc

# create Python3 virtual environment
$ mkvirtualenv cv -p python3

# Install the PiCamera API 
$ pip install "picamera[array]"

Step #4: Compile OpenCV 4 from source 
# download the OpenCV source code for both the opencv and opencv_contrib 
$ cd ~
$ wget -O opencv.zip https://github.com/opencv/opencv/archive/4.1.1.zip
$ wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.1.1.zip
$ unzip opencv.zip
$ unzip opencv_contrib.zip
$ mv opencv-4.1.1 opencv
$ mv opencv_contrib-4.1.1 opencv_contrib

# Increasing your SWAP space will enable compile OpenCV with all four cores 
$ sudo vim /etc/dphys-swapfile 
    # set size to absolute value, leaving empty (default) then uses computed value
    #   you most likely don't want this, unless you have an special disk situation
    # CONF_SWAPSIZE=100
    CONF_SWAPSIZE=2048
$ sudo /etc/init.d/dphys-swapfile stop
$ sudo /etc/init.d/dphys-swapfile start

# Compile and install OpenCV 4 on Raspbian Buster 
# Ensure in the cv virtual environment using the workon command
$ workon cv
# install NumPy(an OpenCV dependency)
$ pip install numpy
# configure build 
$ cd ~/opencv
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D ENABLE_NEON=ON \
    -D ENABLE_VFPV3=ON \
    -D BUILD_TESTS=OFF \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D CMAKE_SHARED_LINKER_FLAGS=-latomic \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D BUILD_EXAMPLES=OFF ..

# compile processing using all four cores
$ make -j4 

# install OpenCV on Raspberry Pi
$ sudo make install
$ sudo ldconfig

# Reset SWAP (Reset CONF_SWAPSIZE to 100MB; Restart the swap service)

# Sym-link OpenCV 4 on the Raspberry Pi 
$ cd /usr/local/lib/python3.7/site-packages/cv2/python-3.7
$ sudo mv cv2.cpython-37m-arm-linux-gnueabihf.so cv2.so
$ cd ~/.virtualenvs/cv/lib/python3.7/site-packages/
$ ln -s /usr/local/lib/python3.7/site-packages/cv2/python-3.7/cv2.so cv2.so

Step 5: Testing OpenCV 4 Raspberry Pi BusterOS install 
$ cd ~
$ workon cv
$ python
>>> import cv2
>>> cv2.__version__
'4.1.1'
>>>
```