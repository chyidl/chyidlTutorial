Caffe Deep Learning Framework
=============================

Section 1: Setting Up Caffe2
----------------------------

* What is Caffe2?
    Caffe2 is A New Lightweight, Modular, and Scalable Deep Learning Framework.

* Setting up dependencies for Caffe2
    - [installCaffe2.sh](/root/mldl/RequirementTutorial/Caffe/installCaffe2.sh)

* Installing Caffe2 on Linux 
    - $ git clone https://github.com/pytorch/pytorch.git && cd pytorch
    - $ git submodule update --init --recursive
    - $ sudo -H python3 setup.py install

* Verifying the installation 
    > Run this to see if your Caffe2 installation was successful.
    - $ cd ~ && python3 -c 'from caffe2.python import core' 2>/dev/null && echo "Success" || echo "Failure"


Testing Caffe2 installation with an image classifier 
```

Section 2: Implementing Neural Networks and Deep Learning 
---------------------------------------------------------

Section 3: Understanding Caffe2 
-------------------------------

Section 4: Understanding a Convolutional Neural Network
-------------------------------------------------------

Section 5: Implementing Weight Initialization, Optimization, and Regulatization
-------------------------------------------------------------------------------

Section 6: Introduction to Recurrent Neural Network
---------------------------------------------------
