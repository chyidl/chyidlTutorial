#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# autofans.py
# AutoControlFans
#
# 🎂"Here's to the crazy ones. The misfits. The rebels.
# The troublemakers. The round pegs in the square holes.
# The ones who see things differently. They're not found
# of rules. And they have no respect for the status quo.
# You can quote them, disagree with them, glority or vilify
# them. About the only thing you can't do is ignore them.
# Because they change things. They push the human race forward.
# And while some may see them as the creazy ones, we see genius.
# Because the poeple who are crazy enough to think thay can change
# the world, are the ones who do."
#
# Created by Chyi Yaqing on 12/25/18 12:16.
# Copyright © 2018. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT
import RPi.GPIO as GPIO
import time
import datetime
import sys
import csv

# Pin Numbering Declaration
#   GPIO.BOARD - Board numbering scheme.
#   GPIO.BCM   - Broadcom chip-specific pin numbers.
GPIO.setmode(GPIO.BCM)

# Control fan ON/OFF
fanPin = 18
fanSpeed = 0
fanSum = 0
pTemp = 10          # PID - P
iTemp = 1           # PID - I
desiredTemp = 45    # not higher than 45 C

# Setting a Pin Mode
# Before you can use it as either an input or output.
# To set a pin mode
GPIO.setup(fanPin, GPIO.OUT)

# PWM ("Analog") Output
# To initialize PWM, use GPIO.PWM([pin], [frequency]) function
pwm = GPIO.PWM(fanPin, 50)
# pwm.start([duty cycle]) to set an initial value
pwm.start(50)

def getCPUTemperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        cputemp = f.readline() # some this like '55123\n'
        cputemp.replace('\n','')
        cputemp = float(cputemp)/1000
        return cputemp # float value


def fanOFF():
    global pwm
    pwm.start(0)


def handleFan():
    global pwm, fanSpeed, fanSum
    actualTemp = getCPUTemperature()
    diff = actualTemp - desiredTemp
    fanSum += diff
    pDiff = diff*pTemp
    iDiff = fanSum*iTemp
    fanSpeed = int(pDiff + iDiff)
    if fanSpeed > 100:
        fanSpeed = 100
    if fanSpeed < 20:
        fanSpeed = 0

    # To adjust the value of the PWM output pwm.ChangeDutyCycle([duty cycle]) function.
    # [duty cycle] can be any value between 0(i.e 0%/LOW) and 100(i.e 100%/HIGH)
    pwm.ChangeDutyCycle(fanSpeed)
    return actualTemp, fanSpeed


if __name__ == '__main__':
    try:
        with open('/home/pi/chyidl.com/AutoControlFans/autafans.csv', 'a+') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_NONE)
            writer.writerow(['Timestamp','Temp', 'Speed'])
            while True:
                temp, speed = handleFan()
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                writer.writerow([now, temp, speed])
                time.sleep(5) # Read temperature every 5 sec
    except KeyboardInterrupt:
        print("You Press Control-c will to exit script!")
        sys.exit(0)
    except Exception as err:
        print(err)
    finally:
        fanOFF()
        # Garbage Collecting to release any resources your script
        GPIO.cleanup()
