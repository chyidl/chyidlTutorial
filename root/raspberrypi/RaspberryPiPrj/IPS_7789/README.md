1.3" IPS Display
================
```
260 ppi, 240x240 pixel
16-bit full color pixels
driver IC: ST7789

This color display uses SPI to receive image data.
That means you need at least 4 pins - clock, data in, tft cs and d/c

1. GND  : Power Ground
2. LEDK : LED Cathode -- GPIO 27 [13] BCM27
3. LEDA : LED Anode
4. VDD  : Power Supply for Analog
5. GND  : Power Ground
6. GND  : Power Ground
7. D/C (DC) -- GPIO24 [18] BCM24 connect to SPI data/command select pin in 4-line serial interface
8. CS (CS)   : Chip selection pin; Low enable, High disable
9. SCL (CLK)  : -- SCLK [23] SCLK This pin is used to be serial interface clock
10. SDA (DIN): -- MOSI [19] MOSI SPI interface input/output pin, the data is latched on the rising edge of the SCL signal
11. RESET (RST): GPIO 25 [22] BCM25 This signal will reset the device and it must be applied to properly initialize the chip. Signal is active low.
12. GND : Power Ground.
```
