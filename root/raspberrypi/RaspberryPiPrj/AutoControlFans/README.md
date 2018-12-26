# Auto-Control Raspberry Pi Fans for Cool using PWM and PID Controller

A good set of fans can keep your computer from overheating, but they can also make your computer sound like a wind tunnel.Here's how to control your Raspi3B fans for superior cooling when it's working hard, and silence when it isn't.

**PWM**: Pulse Width Modulation
**PID**: Proportional Integral Derivative controllers
**MOSFET**: Metal oxide semiconductor field-effect transistor is a type of field effect transistor

![autofans.png](/imgs/raspberrypi/autofans.png?raw=true)

using simple concept: A MOSFET transistor to switch the fan on or off and a Python program which measures the CPU temperature and switched the MOSFET on,when the temperature was too high

please action: MOSFET switch voltage 

- [autofans.py](/root/raspberrypi/RaspberryPiPrj/AutoControlFans/autofans.py)
