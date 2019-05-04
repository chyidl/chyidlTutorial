HomeKit with Homebridge and Raspberry Pi 
========================================
* HomeKit: is a software framework by Apple that lets users set up their iOS Device to configure, communicate with, and control smart-home appliances.

* Homebridge: HomeKit support for the impatient 
> Homebridge is a lightweight NodeJS server you can run on your home network that emulates the iOS HomeKit API. It supports Plugins, which are community-contributed modules that provide a basic bridge from HomeKit to a various 3rd-party APIs provides by manufactures of "smart home" devices.

Basic setup preparations
------------------------
```
begin by updating the default system packages 
$ sudo apt-get update 
$ sudo apt-get upgrade 

may need to install git and make 
$ sudo apt-get install git make
```

Install Node From Package Manager
---------------------------------
```
If you are running a newish Raspberry Pi with an ARMv7 chip or better, you can install Nodejs using their apt-get repository
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash - 
$ sudo apt-get install -y nodejs 
```

Node js Install on Raspberry Pi from Binaries
------------------------------------------------
```
1. Install Node.js on Raspberry Pi 
# first of all type this in your terminal on Raspberry Pi to detect the version that you need:
$ uname -m 

2. Download Node.JS Linux Binaries for ARM 
# Go to [Node.js download page](https://nodejs.org/en/download/) and check right click on the version of ARM that you need and choose Copy Link address. 
# For example I will need ARMv7 
$ wget https://nodejs.org/dist/v10.15.3/node-v10.15.3-linux-armv7l.tar.xz

3. Extract the Archive 
# Using tar that is already installed with the system on your raspberry pi just type this (make sure you change the filename with the file that you have)
$ tar -xvf node-v10.15.3-linux-armv7l.tar.xz

4. Copy Node to /usr/local/node 
$ sudo mkdir -p /usr/local/node 
$ sudo cp -R node-v10.15.3-linux-armv7l/* /usr/local/node/ 
$ sudo update-alternatives --install "/usr/bin/node" "node" "/usr/local/node/bin/node" 1
$ sudo update-alternatives --install "/usr/bin/npm" "npm" "/opt/node/bin/npm" 1

5. Add node path to ~/.zshrc file  
$ vim ~/.zshrc

6. Check if Everything Is Installed Ok 
# Check if node and npm are installed correctly. This lines should print the version of node and npm installed.
$ node -v 
$ npm -v 
```

Install Avahi and other Dependencies 
------------------------------------
```
$ sudo apt-get install libavahi-compat-libdnssd-dev 
```

Running Homebridge on a Raspberry Pi
------------------------------------
```
Quick Overview
	1. Node v4.3.2 or greater is required. Check by running: node --version. 
	2. On Linux only: Install the libavahi-compat-libdnssd-dev package: sudo apt-get install libavahi-compat-libdnssd-dev; 
		Development headers for the Avahi Apple Bonjour compatibility library, Avahi is a fully LGPL framework for Multicast DNS Service Discovery. It allow programs to publish and discover services and hosts running on a local network with no specific configuration.
	3. Install Homebridge using: npm install -g  --unsafe-perm homebridge
	4. Install the plugins using: npm install -g <plugin-name>
		a. homebridge-mi-aqara: a homebridge plugin for XiaoMi Aqara plugin <Aqara is ZigBee gateway with a few sensors>
			Update gateway firmware to 1.4.1_167.0158(gateway v2)
			$ npm install -g homebridge-mi-aqara
            小米网关接入HomeKit/Siri
            I: 获取网关基本信息: 
                获取网关的MAC地址作为网关名称，以及获取网关的局域网通讯协议密码
                Xiaomi Home App -> Mi Home -> Mi Control Hub -> ... -> About -> Quickly click on the blank space of the screen multiple times.
                从网关信息中获取Mac地址xx:xx:xx:xx:xx:xx
                从局域网通信协议中获取密码:xxxxxxxxxxxxxxxx
                将网关Mac地址作为名称，局域网通信协议中的密码作为密码
		b. Install the Raspberry pi Camera 
			$ sudo raspi-config # Go to Interfacing options; Go to Pi Camera; 
			$ sudo modprobe bcm2835-v4l2 
			$ sudo apt install ffmpeg # need to install ffmpeg
			$ npm install -g homebridge-camera-ffmpeg  # And the camera plugin 
        c. Make sure your camera works 
            $ raspistill  # which will create a jpg 
            $ sudo usermod -a -G video $(whoami)
        d. How you disable the power and status LED
            $ sudo sh -c 'echo 0 > /sys/class/leds/led0/brightness'  # Turn off the action LED 
            $ sudo sh -c 'echo 0 > /sys/class/leds/led1/brightness'  # Turn off the power LED 
    5. create config.json file containing your accessories and/or platforms.
        a. On macOS and Linux, the full path for your config.json would be *~/.homebridge/config.json*. Any error messages will contain the exact path where your config is expected to be found.
    6. run Homebridge:
        a. $ homebridge 
    7. Adding Homebridge to iOS 
        a. HomeKit itself is actually not an app, it;s a "database" similar to HealthKit. Where HealthKit has the companion Health app, HomeKit has the Home app, introduced with iOS10.
        b. If you are a member of the iOS deverloper program, you might also find Apple's Catalog app to be useful, as it provides straightforward and comprehensive management of all HomeKit database "objects".
        c. Using the Home app (or most other HomeKit apps), you should be able to add the single accessory "Homebridge", assuming that you're still running Homebridge and you're on the same WiFi network. Adding this accessory will automatically add all accessories and platforms defined in config.json. 
        d. When you attempt to add Homebrige, it will ask for a "PIN code". The default code is like 031-45-154 
    8. Interacting with your Devices
        a. Once your device has been added to HomeKit, you should be about to tell Siri to control your devices. However, realize that Siri is a cloud service, and iOS may need some time to synchronize your device information with iCloud.
```

Setup Homebridge to Start on Bootup
-----------------------------------
> Using systemd to start Homebridge on bootup, I prefered this method because it will restart if an error occurs.
* Here are the steps that worked for me:
    - 1. $ sudo vim /etc/default/homebridge and paste this 
    - [homebridge](/root/raspberrypi/RaspberryPiPrj/homebridgeHomeKitRaspberryPi/homebridge)
    - 2. $ sudo vim /etc/systemd/system/homebridge.service and paste this 
    - [homebridge.service](/root/raspberrypi/RaspberryPiPrj/homebridgeHomeKitRaspberryPi/homebridge.service)
    - 3. Create a user to run service: sudo useradd --system homebridge 
    - 4. $ sudo mkdir /var/homebridge 
    - 5. $ sudo cp ~/.homebridge/config.json /var/homebridge/
    - 6. $ sudo cp -r ~/.homebridge/persist /var/homebridge 
    - 7. $ sudo chmod -R 0777 /var/homebridge 
    - 8. $ sudo systemctl daemon-reload 
    - 9. $ sudo systemctl enable homebridge 
    - 10. $ sudo systemctl start homebridge 
   
![HomeKit DEMO image](/imgs/raspberrypi/HomeKit/homekit_demo.png?raw=true)
