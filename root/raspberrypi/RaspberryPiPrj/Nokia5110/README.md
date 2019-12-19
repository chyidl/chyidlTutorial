Nokia 5110/3310 LCD Connected to Raspberry Pi
=============================================
> The Nokia 5110/3310 display is a great inexpensive graphical display.

Wiring
------
```
Need to connect the LCD's SCLK, DIN, and CS pins to the board's SPI pins, and the LCD's RST and D/C pins to free digital I/O pins. with this setup can use the very fast hardware SPI support.

Raspberry Pi 
> To connect the LCD to a Raspberry Pi, the Pi's hardware SPI pins and two GPIO pins should be wired to the LCD as follows:
```

| Raspberry Pi         | Nokia 5110/3310 LCD |
| :------------------- | ------------------: |
| Pin 17 (3v3 Power)   |             LCD VCC |
| Pin 14 (Ground)      |             LCD GND |
| Pin 16 (GPIO)        |             LCD D/C |
| Pin 18 (GPIO)        |             LCD RST |
| Pin 19 (SPI0 - MOSI) |             LCD DIN |
| Pin 23 (SPI0 - SCLK) |             LCD CLK |
| Pin 24 (SPI0 - CEO)  |              LCD CE |

```
The above wiring will support talking to the LCD over the /dev/spidev0.0 interface.
```
 
Dependencies
-----------
> Before using the library you will need to make sure you have a few dependencies installed.
```
$ sudo apt-get install python3-pip python3-dev build-essential
$ sudo pip3 install RPi.GPIO
$ sudo apt-get install python3-pil 

Now to download and install the Nokia LCD python library code and examples, execute the following commands
$ sudo apt-get install git 
$ git clone https://github.com/adafruit/Adafruit_Nokia_LCD.git 
$ cd Adafruit_Nokia_LCD
$ sudo python3 setup.py install 
```

Raspberry Py SPI SetUp
-----------------------
```
$ sudo raspi-config 
Check the files /dev/spidev0.0 and /dev/spidev0.1 are now available 
```
![python image.py](/root/raspberrypi/RaspberryPiPrj/Nokia5110/image.py)
![python lcd_stat.py](/root/raspberrypi/RaspberryPiPrj/Nokia5110/lcd_stat.py)
