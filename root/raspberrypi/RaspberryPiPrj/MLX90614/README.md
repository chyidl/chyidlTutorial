# MLX90614  Infrared Thermometer

## MLX90614 Overview 

Internally, the MLX90614 is a pairing of two devices: an infrared thermopile detector and a signal-confitioning application processor.

Per the Stefan-Boltzman law, any object that isn't below absolute zero (0⁰K) emits (non-human-eye-visible)light in the infrared spectrum that is directly proportional to its temperature.The special infrared themopile inside the MLX90614 senses how much infrared energy is being emiited by materials in its field of view, and produces an electrical signal proportional to that.

![ MLX90614 internal block digram ](/imgs/raspberry/MLX90614_internal_block_digram.png?raw=true)

## MLX90614 Pinout 

The MLX90614 comes in an TO-39 "can" package with four legs: two for power, and two for the SMBus interface. A "notch" on the package helps to indicate which pin is which.

![ MLX90614 pinout ](/imgs/raspberry/mlx90614-pinout.png?raw=true)

## Capabilities

The MLX90614 produces two temperature measurements: an object and an ambient reading. The **object temperature** is the non-contact measurement you'd expect from the sensor, while the **ambient temperature** measures the temperature on the die of the sensor. The ambient can be useful to calibrate the data, but the real meat of our readings will come from the object temperature measurement.

The object temperature measurements can range from -70 to 382.2 ⁰C (-94 to 719.96 ⁰F), while the ambient temperature reading ranges from -40 to 125 ⁰C.

Both the ambient temperature and object temperatures have a resolution of 0.02 ⁰C.

## Reading MLX90614 IR sensor 

```
# install the i2c-tools package by:
$ sudo apt-get install i2c-tools

# Reboot the machine by:
$ sudo shutdown -r now 

# test to see any device connected by:
$ sudo i2cdetect -y 1

# You should see something like this:
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- 5a -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --          

# Next install the python3-smbus python module 
$ sudo apt-get install python3-smbus 
```

- [ir_sensor.py](/root/raspberrypi/RaspberryPiPrj/MLX90614/ir_sensor.py)
