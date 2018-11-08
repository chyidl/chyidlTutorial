# Boost C++ Library - Getting Started on Unix Vatriants 

## 1. Get Boost 

1. Download boost_1_68_0.tar.bz2
2. tar --bzip2 -xf boost_1_68_0.tar.bz2 

## 2. The Boost Distribution 

This is a sketch of the resulting directory structure:

## 3. Header-Only Library 

Most Boost libraries are header-only; they consist entirely of header files containing templates and inline function, and require no separately compiled library binaries or special treatment when linking.

## 4. Prepare to Use a Boost Library Binary 

4.1 Easy Build and Install
```
$ cd path/to/boost_1_68_0 
$ ./bootstrap.sh --help 

Select your configuration options and invoke ./bootstrap.sh again without the --help option. Unless you have write permission in your system's **/usr/local/** directory, you'll probably want to at least use.

$ ./bootstrap.sh --prefix=/usr/local/ --with-python=/usr/bin/python3 

Finally
$ ./b2 install
```
