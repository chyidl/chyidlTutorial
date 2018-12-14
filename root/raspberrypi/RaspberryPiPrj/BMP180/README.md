# BMP180 Barometric Pressure|Temperature

## DESCRIPTION 

This precision sensor from Bosch is the best low-cost sensing solution for measuring baronmetric pressure and temperature. Because pressure changes with altitude you can also use it as an altimeter! The sensor is soldered onto PCB with 3.3V regulator, I2C level shifter and pull-up resistors on the I2C pins.

The BMP180 is the next-generation of sensors from Bosch, and replaces the BMP085. 

## Technical Details 

Vin: 3 to 5 VDC
Logic: 3 to 5V compliant 
Pressure sensing range: 300-1100 hPa (9000m to -500m above sea level)
Up to 0.03hPa / 0.25m resolution 
-40 to 85⁰C operational range, ±2⁰C temperature accuracy 
This board/chip uses I2C 7-bit address 0x77 

## I2C Activation 

```
Since the BMP180 sensor works via the I2C bus, Now we install three more needed tools 
$ sudo apt-get install python3-smbus i2c-tools git  

$ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- 77   
```
