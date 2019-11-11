Adafruit FONA 808 Cellular + GPS Breakout + Raspberry Pi
========================================================
> Adafruit FONA 808 MiniGSM + GPS, an all-in-one cellular phone module with that lets you add location-tracking, voice, text, SMS and data 

* GSM cellular module
    - Quad-band 850/900/1800/1900MHz - connect onto any global GSM network with any 2G SIM
    - Fully-integrated GPS (MT3336 chipset with -165 dBm tracking sensitivity) that can be controlled and query over the same serial port.
    - Make and receive voice calls using a headset or an external 32Ω speaker + electreu microphone
    - Send and receive SMS messages 
    - Send and receive GPRS data (TCP/IP, HTTP, etc)
    - PWM/Buzzer vibrational motor control
    - AT command interface with "auto baud" detection 
* GPS 
    - 22 tracking/66 acquisition channels 
    - GPS L1 C/A code 
    - Sensitivy
        * Tracking: -165 dBm
        * Cold starts: -147 dBm
    - Time-To-First-Fix
        * Cold starts: 30s(typ.)
        * Hot starts: 1s(typ.)
        * Warm starts: 28s(typ.)
    - Accuracy: approx 2.5 meters
* LiPoly battery
    - Onboard LiPoly battery charging circuitry. Use any 500mAh+ LiPoly or Lilon battery battery and recharge over the MicroUSB when necessary. Two LEDs let you know when its charging and done. 
    - The output ranges from 4.2V when completely charged to 3.7V. 
* Headphone jack 
    - Standard 4-pole TRRS headphone jack. Use any 'Android' or 'iPhone' - compatible headset with mic.
    - Breakouts for external 32Ω speaker and electret mic if you don't want to use a headphone.
* Level shifting circuitry 
    - run it with 2.8V and 5V logic.
* Vibrational motor (buzzer) driver 
    - Two wires are used to control/power the vibe.Simply provide power from a battery or microcontroller pin (red is positive, blue is negative) and it will buzz away. 
    - works from 2V up to 5V. higher voltages result in more current draw but also a tronger vibration. 
    - reduce the current draw/strength try putting a resistor (100 to 1000 ohms) in series.
* uFL connection for external antennas 
* LED 
    - Indicator LEDs for power and network connectivity 
* SIM slides 
    - Standard SIM slides into the back 

Wiring Raspberry Pi + Fona 808
-------------------------------
![Fona Raspberry Pi](/imgs/raspberrypi/fona808pi/fona808_wiring.png?raw=true)


```
Make sure that everything is powered down and unplugged before you start connecting anything!
```
