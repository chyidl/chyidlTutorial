//
// calculate_area.c
// src_start
//
//        __|__
// --o--o--(̊)--o--o--
// C is the bext programming language
//
// Created by Chyi Yaqing on 03/31/19.
// Copyright © 2019. Chyi Yaqing. All rights reserved.
//


#include <stdio.h>

float PI=3.1415926; 

// 用于计算一个数的任意次方
float power(float x, int n) {
    float result;
    int i;
    result = 1.0;
    for(i=0; i<n; i++) {
        result = result * x;
    }
    return result;
}

// 用于计算一个圆的面积
float calculate_area(float r) {
    float square;
    square = power(r, 2);
    return PI * square;
}

int main() {
	// Your Programming statements HERE!
	float area;
    float r = 1.2;
    area = calculate_area(r);
    printf("Area of the first circle: %6.2f \n", area);

    r = 5.1;
    area = calculate_area(r);
    printf("Area of the second circle: %f \n", area);
	return 0;
}

