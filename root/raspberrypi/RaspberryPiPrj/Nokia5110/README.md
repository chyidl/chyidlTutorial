Nokia 5110/3310 LCD 
===================

The Nokia 5110/3310 display is a great inexpensive graphical display.

I general you will need to connect the LCD's SCLK, DIN, and CS pins to the board's SPI pins, and the LCD's RST and D/C pins to free digital I/O pins. 

Dependencies
-----------
```
$ sudo apt-get install python3-pip python3-dev build-essential
$ sudo pip3 install RPi.GPIO
$ sudo apt-get install python3-imaging 

Now to download and install the Nokia LCD python library code and examples, execute the following commands
$ sudo apt-get install git 
$ git clone https://github.com/adafruit/Adafruit_Nokia_LCD.git 
$ cd Adafruit_Nokia_LCD
$ sudo python3 setup.py install 

Raspberry Py SPI SetUp
    Check the files /dev/spidev0.0 and /dev/spidev0.1 are now available 
```
![python image.py](/root/raspberrypi/RaspberryPiPrj/Nokia5110/image.py)
