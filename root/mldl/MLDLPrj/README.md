Machine Learning & Deep Learning
================================

Getting started with Computer Vision, Deep Learning, and OpenCV
---------------------------------------------------------------

* Step #1: Install OpenCV + Python
```
# Install OpenCV 4 on macOS 

Step #1: Install Xcode 
    After Xcode has installed we need to accept a license agreement.
    $ sudo xcodebuild -licese 

    Once you've accepted the license agreement, install Apple Command Line Tools
    $ sudo xcode-select --install 

Step #2: Install Homebrew 
    install the Mac community package manager, Homebrew 
    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

    update the Homebrew definitions 
    $ brew update 

    edit your profile with vim using the following command:
    $ vim ~/.zshrc 

    append the following lines to the end to update your PATH
        # Homebrew 
        export PATH=/usr/local/bin:$PATH 

Step #3: Install OpenCV prerequisites using Homebrew
    Install Python3.7 
    $ brew install python3

    verify python version 
    $ python3
Python 3.7.4 (default, Sep  7 2019, 18:27:02)
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
    $ which python3 
/usr/local/bin/python3
    
    Install other prerequisties(1. tools used to build and compile; 2.libraries used for image I/O operations; 3.optimization libraries)
    $ brew install cmake pkg-config 
    $ brew install jpeg libpng libtiff openexr 
    $ brew install eigen tbb 

    All wget does is download files from the command line.
    $ brew install wget

Step #4: Install Python dependencies for OpenCV 4
    install pip (a Python package manager)
    $ wget https://bootstrap.pypa.io/get-pip.py 
    $ sudo python3 get-pip.py 
    
    install virtualenv and virtualenvwrapper, two tools for managing virtual environments. Python virtual environments are a best practice for Python development.
```

Python Virtual Environments: A Primer
-------------------------------------

* Why the Need for Virtual Environments?
```
Python, like most other modern programming languages, has its own unique way of downloading, storing, and resolving packages (or modules). 

# Most system packages are stored in a child directory of the path stored in sys.prefix
Python 3.7.4 (default, Sep  7 2019, 18:27:02)
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.prefix
'/usr/local/Cellar/python/3.7.4_1/Frameworks/Python.framework/Versions/3.7'
>>>

# More relevant to the topic of this article, third party packages installed using easy_install or pip are typically placed in one of the directories pointed to by site.getsitepackages
>>> import site
>>> site.getsitepackages()
['/usr/local/Cellar/python/3.7.4_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages']
>>>

This is where virtual environments and the virtualenv/venv tools come into play...
```

* What is a Virtual Environment?
```
The Main purpose of Python virtual environments is to create an isolated environment for Python projects. This means that each project can have its own dependencies, regardless of what dependencies every other project has.

```
