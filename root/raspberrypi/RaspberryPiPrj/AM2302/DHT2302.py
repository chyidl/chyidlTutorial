#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
import sys 
import time 
import datetime 
import Adafruit_DHT 

# Parse command line parameters
sensor_args = {
    '11': Adafruit_DHT.DHT11,
    '22': Adafruit_DHT.DHT22,
    '2302': Adafruit_DHT.AM2302
}

def get_humidity_temperature(sensor, pin):
    
    while True:
        # Try to grab a sensor reading, Use the read_retry method which will retry up 
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
        # Un-comment the line below to convert the tenperature to Fahrenheit
        # temperature = temperature * 9/5.0 + 32 
    
        # Note the sometimes you won't get a reading and 
        # the results will be nill (because Linux can't
        # guarantee the timming of calls to read the sensor).
        # If this happens try again!
        if humidity is not None and temperature is not None:
            print('DateTime= {0} Temp={1:0.2f}℃ Humidity={2:0.2f}%'.format(datetime.datetime.now().strftime("%H:%M:%S"),temperature, humidity))
            return (temperature, humidity)
        else:
            print('Failed to get reading. Try again!')
            time.sleep(2) 

if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
        sensor = sensor_args[sys.argv[1]]
        pin = sys.argv[2]
    else:
        sensor = Adafruit_DHT.AM2302
        pin = 4

    with open("shanghai_houses_DHTAM2302.csv", "a", buffering=1, encoding='utf-8') as log:
        while True:
            try:
                temperature, humidity = get_humidity_temperature(sensor, pin)
                log.write("{0},{1},{2}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(temperature), str(humidity)))
            except IOError as err:
                print(err)
            finally:
                time.sleep(2)

    
