#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import datetime
import sys, os
import time

from bluepy.btle import BTLEException
from bluepy.sensortag import SensorTag
import csv


# configurations to be set accordingly
SENSORTAG_ADDRESS = "24:71:89:E8:4D:87"
FREQUENCY_SECONDS = 5  # it takes about 4-5 seconds to obtain readings and upload to google sheets


def enable_sensors(tag):
    """Enable sensors so that readings can be made."""
    tag.IRtemperature.enable()
    tag.accelerometer.enable()
    tag.humidity.enable()
    tag.magnetometer.enable()
    tag.barometer.enable()
    tag.gyroscope.enable()
    tag.keypress.enable()
    tag.lightmeter.enable()
    tag.battery.enable()

    # Some sensors (e.g., temperature, accelerometer) need some time for initialization.
    # Not waiting here after enabling a sensor, the first read value might be empty or incorrect.
    time.sleep(1.0)


def disable_sensors(tag):
    """Disable sensors to improve battery life."""
    tag.IRtemperature.disable()
    tag.accelerometer.disable()
    tag.humidity.disable()
    tag.magnetometer.disable()
    tag.barometer.disable()
    tag.gyroscope.disable()
    tag.keypress.disable()
    tag.lightmeter.disable()
    tag.battery.disable()


def get_readings(tag):
    """Get sensor readings and collate them in a dictionary."""
    try:
        enable_sensors(tag)
        readings = {}
        # IR sensor
        readings["ir_temp"], readings["ir"] = tag.IRtemperature.read()
        # humidity sensor
        readings["humidity_temp"], readings["humidity"] = tag.humidity.read()
        # barometer
        readings["baro_temp"], readings["pressure"] = tag.barometer.read()
        # luxmeter
        readings["light"] = tag.lightmeter.read()
        # battery
        readings["battery"] = tag.battery.read()

        disable_sensors(tag)

        # round to 2 decimal places for all readings
        readings = {key: round(value, 2) for key, value in readings.items()}
        return readings
    except BTLEException as error:
        print("Unable to take sensor readings. {}".format(error))
        return {}


def reconnect(tag):
    try:
        tag.connect(tag.deviceAddr, tag.addrType)
    except Exception as error:
        print("Unable to reconnect to SensorTag.")
        raise error


def append_readings(worksheet, readings):
    """Append the data in the spreadsheet, including a timestamp."""
    try:
        with open(worksheet, 'a', newline='') as csvfile:
            # remove erroneous readings
            if (readings["humidity_temp"] < readings["ir_temp"] - 2 or
                        readings["humidity_temp"] > readings["ir_temp"] + 2):
                readings["humidity_temp"] = ''
            if readings["humidity"] < 1 or readings["humidity"] > 99:
                readings["humidity"] = ''
            columns = ["ir_temp", "humidity_temp", "baro_temp", "ir", "humidity", "pressure", "light", "battery"]
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
            # check worksheet is exist row data
            if os.stat(worksheet).st_size == 0:
                spamwriter.writerow(["datetime", "ir_temp", "humidity_temp", "baro_temp", "ir", "humidity", "pressure", "light", "battery"])
            spamwriter.writerow([datetime.datetime.now()] + [readings.get(col, '') for col in columns])
            print("Wrote a row to {0}".format(worksheet))

    except Exception as error:
        print("Append error, {}".format(error))


def main():
    print('Connecting to {}'.format(SENSORTAG_ADDRESS))
    tag = SensorTag(SENSORTAG_ADDRESS)
    worksheet = "TensorTagCC2650.csv"
    print('Logging sensor measurements to {0} every {1} seconds.'.format(worksheet, FREQUENCY_SECONDS))
    print('Press Ctrl-C to quit.')
    while True:
        # get sensor readings
        readings = get_readings(tag)
        if not readings:
            print("SensorTag disconnected. Reconnecting.")
            reconnect(tag)
            continue

        # print readings
        print("Time:\t{}".format(datetime.datetime.now()))
        print("IR reading:\t\t{}, temperature:\t{}".format(readings["ir"], readings["ir_temp"]))
        print("Humidity reading:\t{}, temperature:\t{}".format(readings["humidity"], readings["humidity_temp"]))
        print("Barometer reading:\t{}, temperature:\t{}".format(readings["pressure"], readings["baro_temp"]))
        print("Luxmeter reading:\t{}".format(readings["light"]))
        print("Battery reading:\t{}".format(readings['battery']))
        append_readings(worksheet, readings)
        time.sleep(FREQUENCY_SECONDS)


if __name__ == "__main__":
    main()
