#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import smbus
import time

port = 1
bus = smbus.SMBus(port)
device_address = 0x5a

while True:
    try:
        reading = bus.read_word_data(device_address, 0x07)
        temp = reading * 0.02 - 273.15
        print("temp: {} ⁰C".format(round(temp,2)))
    except IOError:
        pass
    finally:
        time.sleep(1)

