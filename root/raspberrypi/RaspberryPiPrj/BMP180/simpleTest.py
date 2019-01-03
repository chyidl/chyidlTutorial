#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import BMP180 as BMP180
import time

# Default constructor will pick a default I2C bus.
#
sensor = BMP180.BMP180()

while True:
    print('Temp = {0:0.2f} ⁰C'.format(sensor.read_temperature()))
    print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
    print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
    print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))
    time.sleep(1)
