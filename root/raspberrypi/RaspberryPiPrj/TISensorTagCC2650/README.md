TI Sensor Tag CC2650 and Raspberry Pi 
=======================================

Design Features
-----------------

* Offers Cloud Connectivity Out of Box 
    - Access and Control Your SensorTag From Anywhere and Explore a Seamless Integration With Mobile Applications and Web Pages Through JavaScript and MQTT
* Supports Multi-Standard Wireless MCU 
    - Bluetooth Smart
    - ZigBee
    - IPv6 over low-power wireless personal area networks(6LoWPAN)
* Offers Low Power
* Supports 10 Low-Power Sensors
    - Ambient Light 可见光  -- OPT30001 
    - Infrared Temperature 红外温度
    - Ambient Temperature  环境温度
    - Accelerometer 加速度计
    - Gyroscope 陀螺仪
    - Magnetometer 磁力计
    - Pressure 压力计
    - Humidity 湿度计
    - Microphone 话筒
    - Magnetic Sensor 磁传感器
* Based on the Extremely Low-Power and High-Performance ARM@Cortex-M3 CC2650 Wireless MCU

![# TI Sensor Tag CC2650](/imgs/raspberrypi/cc2650.png?raw=true)

Highlighted Products
--------------------

* CC2650 - Wireless MCU 
    - The CC2650 device is a wireless MCU targeting Bluetooth Smart, ZigBee and 6LoWPAN, and ZigBee RF4CE remote control applications.
    - The device is a member of the CC26xx family of cost-effective, ultra-low power, 2.4-GHz RF devices. The ability to consume very low active RF and MCU currents and low-power mode currents provides excellent battery life for the device. This ability alos lets the device operate on small coin cell batteries and in energy-harvesting applications.

![# TI Sensor Tag CC2650 Wireless MCU](/imgs/raspberrypi/CC2650-MCU.png?raw=true)

* OPT30001 - Ambient light Sensor 
    - The OPT3001 sensor measures the intensity of visible light. The spectral response of the sensor closely matches the photopic of the human eye and includes infrared rejection.

![# OPT3001 - Ambient Light Sensor](/imgs/raspberrypi/OPT3001.png?raw=true)

* TMP007 - Infrared Thermopile Temperature Sensor
    - The TMP007 sensor is an IR thermopile sensor that measures the temperature of an object without direct contact with it. The integrated thermopile absorbs the infrared energy from the object in the field of view of the sensor. The device digitizes the thermopile voltage and the provides it and the die temperature as inputs to the integrated math engine. The main engine then computes the temperature of the corresponding object.

![# TMP007 - Infrared Thermopile Temperature Sensor](/imgs/raspberrypi/TMP007.png?raw=true)

* HDC1000 - Humidity Sensor With Integrated temperature Sensor
    - The HDC1000 sensor is a factory-calibrated digital humidity sensor with an integrated temperatures sensor that provide accurate measurements at very power. The HDC1000 sensor measures humidity based on a novel capacitive sensor and functions within thetemperature range of -40C to 125C. The innovative WLCSP (wafer-level chip scale package) simplifies board design with an ultra compact package and the sensing element on the bottom of the HDC1000 device protects against dirt,dust,and other contaminants.
    
![# HDC1000 - Humidity Sensor With Integrated Temperature Sensor](/imgs/raspberrypi/HDC1000.png?raw=true)


Raspberry Pi Install Bluez
---------------------------

* Get the latest version of Bluez
    - Bluez( the Bluetooth Stack for Linux) 
    - $ wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.50.tar.xz
    - Before installing Bluez, the Raspberry Pi environment needs to be updated to have the following set of libraries
    - $ sudo apt-get install libglib2.0-0 libglib2.0-dev libdbus-1-dev libudev-dev libical-dev libreadline-dev libusb-1.0-0-dev 
    - $ tar -xzvf bluez-5.50.tar.xz 
    - $ cd bluez-5.50 &&  sudo ./configure --prefix=/usr --mandir=/usr/share/man --sysconfdir=/etc --localstatedir=/var --with-systemdsystemunitdir --with-systemduserunitdir --enable-library
    - $ make -j4 && sudo make install
    - $ we shall use **hcitool** and **gatttool** to discover bluetooth addresses of the bluetooth enabled devices.
* Scan to discover the TI Sensor Tag CC2650 
    - $ sudo hciconfig hci0 up # activate the bluetooth port
    - $ sudo hcitool lescan # Scan for bluetooth enabled devices near to the Raspberry Pi devices.
    - 24:71:89:E8:4D:87 CC2650 SensorTag # Note down the bluetooth address for the Sensor Tag
* Pair Raspberry Pi With TI Sensor Tag 
    - use Bluezs **gatttool** to pair the Raspberry Pi With TI Sensor Tag and enlist it for service provided by the SensorTag in order to read sensor data.
    - Establish an interactive session:
    ```
    Syntax
    $ gatttool -b [bluetooth_adr] --interactive 
    
    Command 
    $ gatttool -b 24:71:89:E8:4D:87 -I 
    
    Once the session is open, will see a command prompt as follows:
    $ gatttool -b 24:71:89:E8:4D:87 -I
      [24:71:89:E8:4D:87][LE]> connect
      Attempting to connect to 24:71:89:E8:4D:87
      Connection successful
      [24:71:89:E8:4D:87][LE]>
    ```
* Retrieving Temperature from SensorTag on to Raspberry Pi
    - The TI Sensor Tag includes 10 low-power MEMS sensors (light, digital micriphone, magnetic sensor, humidity, pressure, accelerometer, gyroscope, magnetometer, object temperature, and ambient temperature)
    - To retrieve temperature data onto your Raspberry Pi, you should enable the temperature sensor(s) on TI CC2650, so that it starts measuring the temperature. This data or the reading is held in a temperature designated handle and you need to read it from this handle.
    - Enable the Temperature Sensor
    ```
    # This activates the temperature sensors on TICC2650, which were in standby mode
    [24:71:89:E8:4D:87][LE]> char-write-cmd 0x24 01 
    
    # Now read-notification for the IR-Temperature data in hexadecimal values from this handle 
    [24:71:89:E8:4D:87][LE]> char-read-hnd 0x21 

    # You should see both IR and Ambient Temperature outputs in Hexadecimal format:
    Characteristic value/descriptor: 04 00 ad 27 01 11 31
    ```    
- [SensorTag CC2650](/root/raspberrypi/RaspberryPiPrj/TISensorTagCC2650/sensortag_weather.py)