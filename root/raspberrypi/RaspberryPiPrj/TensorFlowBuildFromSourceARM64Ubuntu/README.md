Tensorflow Build from source on Raspberry Pi Ubuntu 18.04(aarch64)
==================================================================

Step for Linux (Install the following build tools to configure your developement environment.)
----------------------------------------------------------------------------------------------

* Install Python and the TensorFlow package dependencies
```
(Ubuntu) $ sudo apt install python3-dev python3-pip

$ sudo -H python3 -m pip install six numpy wheel setuptools mock 
$ sudo -H python3 -m pip install keras_applications keras_preprocessing 
REQUIRED_PACKAGES = [
    'absl-py >= 0.7.0',
    'astor >= 0.6.0',
    'gast >= 0.2.0',
    'google_pasta >= 0.1.6',
    'keras_applications >= 1.0.6',
    'keras_preprocessing >= 1.0.5',
    'numpy >= 1.14.5, < 2.0',
    'six >= 1.10.0',
    'protobuf >= 3.6.1',
    'tensorboard >= 1.13.0, < 1.14.0',
    'tensorflow_estimator >= 1.13.0rc0, < 1.14.0rc0',
    'termcolor >= 1.1.0',
    'wrapt >= 1.11.1',
]
```

* Install Bazel
```
Bazel: the build tool used to compile TensorFlow. 
And the location of the Bazel executable to your PATH environment variable.

```
