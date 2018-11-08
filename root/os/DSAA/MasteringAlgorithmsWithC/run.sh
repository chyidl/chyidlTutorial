#!/bin/bash

if [ ! -d "build" ];then
    mkdir build
fi

if [ -d "MasterAlgorithmsWithC/Example/$1" ];then
    cc MasterAlgorithmsWithC/source/*.c ./MasterAlgorithmsWithC/Example/$1/main.c -I MasterAlgorithmsWithC/include -o build/$1
    cd build
    ./$1
else
    echo "./MasterAlgotithmsWithC/Example does not exists."
    echo "./MasterAlgotithmsWithC/Example list :"
    echo `ls MasterAlgotithmsWithC/Example`
fi
