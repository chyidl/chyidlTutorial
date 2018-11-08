# AM2302 Temperature and humidity

## About

AM2302 capacitive humidity sensing digital temperature and humidity module is one that contains the compound has been calibrated digital signal output of the temperature and humidity sensors.

## DHT22 (AM2302)

- Low cost 
- 3 to 5V power and I/O 
- 2.5mA max current use during conversion (while requesting data)
- Good for 0-100% humidity readings 2-5% accuracy 
- Good for -40 to 80℃  temperature readings 〄0.5℃ accuracy 
- No more than 0.5Hz sampling rate (once every 2 seconds)

## Raspberry Pi Wiring

- GPIO pin #4 
- For DHT11 and DHT22 sensors, don't forget to connect a 4.7K - 10K resistor from the data pin to VCC 

## Software Install(Updated)

- [Adafruit Python DHT](https://github.com/adafruit/Adafruit_Python_DHT)

Use some C code to talk to the DHT sensors since they require extremely fast timing to read, and then wrap the C code in a simple Python library for easy integration into your own programs 

```
$ git clone https://github.com/adafruit/Adafruit_Python_DHT.git 
$ cd Adafruit_Python_DHT 

$ sudo apt-get update 
$ sudo apt-get install build-essential python3-dev python3-openssl 

$ sudo python3 setup.py install 
```

This should compile the code for the library and install it on your device so any Python program can access the Adafruit_DHT python module.

- [DHT2302.py](/root/raspberrypi/RaspberryPiPrj/AM2302/DHT2302.py)
