Adafruit FONA 808 Cellular + GPS Breakout + Raspberry Pi
========================================================
> Adafruit FONA 808 MiniGSM + GPS, an all-in-one cellular phone module with that lets you add location-tracking, voice, text, SMS and data 

Terminology
-----------
* GSM(Global System for Mobile Communications) is a standard for second generation or 2G cellular phone networks. The GSM standard replaced the 1st generation analog cell phone networks a number of years ago. Although GSM is now an old standard, GSM networks are still prevalent and available almost anywhere around the world.

* GPRS(General Packet Radio Service) is a standard for sending data over a GSM cellular network. FONA supports a 2G GRPS data connection.

* PPP (Point-to-Point Protocol) is an old standard for connecting a computer to a network through a serial link. You might have used PPP to connect your computer to the internet through a serial modem or DSL connection years ago! With FONA a PPP connection can be created to talk to the GPRS network through FONA's serial connection with your hardware.

* APN (Access Point Name) is a name to identify the gateway between a GRPS network and the internet. You will need to find the APN for the cellular network you're using with FONA.

* GSM
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
> Setup a serial connection between the Fona and the Raspberry 
![Fona Raspberry Pi](/imgs/raspberrypi/fona808pi/fona808_wiring.png?raw=true)
```
Make sure that everything is powered down and unplugged before you start connecting anything!
    Connect the Fona's GND to the Pi's GND (Row 2, Pin 3) AND the Fona's Key(I ended up soldering 3 tie lines together to do this, but you can prototype with a breadboard)
    Connect the Fina's Key to the Pi;s GND 
        - Note this wiring will force FONA to stay active all the time the Raspberry Pi has power.
    Connect the Fona's Vio to the Pi's 3.3V power (Row 1, Pin 1)
    Connect the Fona's TX to the Pi's RX(Row 2, Pin 5)
    Connect the Fona's RX to the Pi's TX(Row 2, Pin 4)
    Connect the cellular antenna now  - it is labeled "GSM ANT" on the Fona 
    Connect the Fona and Pi with the micro-USB to USB cabel 
    Connect the Lipoly battery to the Fona 
Power on the Pi and the Fona should light up, with a solid blue LED and slow blinking red LED.

The Fona with Pi because it communicates with a serial connection (hence the UART pins, TX, RX). 
By default any Raspberry Pi uses its hard-ware serial pins for the kernel serial console. so this needs to be disabled.

$ sudo vim /boot/config.txt 
    enable_uart=1   # Add this line to the end of the file 
$ reboot

# To test the serial connection, we are going to install PPP and the serial console "screen"
$ sudo apt-get update 
$ sudo apt-get install ppp screen 
$ sudo screen /dev/serial0 115200 
> AT  # Type in 
< OK  # FONA talking back
> Ctrl-A and typing :quit 

Using the Cellular Connection 
> This cellular connection is 2G, so it's only 5-10 kilobytes/second of download speed. You won't be surfing the web with it, but you can talk to internet services, tweet, and text just fine!

Cellular Setup 
$ sudo -i
$ cd /etc/ppp/peers/
$ vim fona
    # Example PPPD configuration for FONA GPRS connection on Debian/Ubuntu.

    # MUST CHANGE: Change the -T parameter value **** to your network's APN value.
    # For example if your APN is 'internet' (without quotes), the line would look like:
    # connect "/usr/sbin/chat -v -f /etc/chatscripts/gprs -T internet"
    connect "/usr/sbin/chat -v -f /etc/chatscripts/gprs -T ****"

    # MUST CHANGE: Uncomment the appropriate serial device for your platform below.
    # For Raspberry Pi use /dev/ttyAMA0 by uncommenting the line below:
    #/dev/ttyAMA0
    # For BeagleBone Black use /dev/ttyO4 by uncommenting the line below:
    #/dev/ttyO4

    # Speed of the serial line.
    115200

    # Assumes that your IP address is allocated dynamically by the ISP.
    noipdefault

    # Try to get the name server addresses from the ISP.
    usepeerdns

    # Use this connection as the default route to the internet.
    defaultroute

    # Makes PPPD "dial again" when the connection is lost.
    persist

    # Do not ask the remote to authenticate.
    noauth

    # No hardware flow control on the serial link with FONA
    nocrtscts

    # No modem control lines with FONA.
    local

Cellular Testing 
$ sudo pon fona     # To turn on the Fona PPPD connection
$ cat /var/log/syslong | grep pppd 
$ ifconfig  # Check if the ppp network interface with 
$ ping baidu.com    # test if your connection is working by pinging 

Reading from the GPS 
    How can you collect GPS data from the Fona and still use the cellular connection (handled by PPPD) to stream that data?
    Fona 808 v1 uses GPS, the Fona 808 v2 uses GNS.
$ sudo poff fona    # Make sure that the PPPD connection is turned off 
$ sudo screen /dev/serial0 115200   # start screen 
> AT 
< OK
> AT+CGNSPWR?   # check if the GPS is on. 
> AT+CGNSPWR=1  # turn on the GPS 
> AT+CGNSINF    # +CGNSINF <GNSS run status>,<Fix status>,<UTC date & Time>,<Latitude>,<Longitude>, <MSL Altitude>,<Speed Over Ground>,<Course Over Ground>,<Fix Mode>,<Reserved1>,<HDOP>,<PDOP>,<VDOP>,<Reserved2>,<GNSS Satellites in View>,<GNSS Satellites Used>,<GLONASS Satellites Used>,<Reserved3>,<C/N0 max>,<HPA>,<VPA>

Streaming GPS Data 
We are going to alternate between turning the PPPD cell service on and streaming, and reading from the GPS.

https://www.digikey.com/en/maker/projects/cellular-gps-enabled-pi-3-fona-pi-3/d0cf660bfc144842a49bfbc5c1dc2ff0

```

