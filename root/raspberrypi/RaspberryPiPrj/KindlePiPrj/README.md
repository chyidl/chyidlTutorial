Kindle + Raspberry Pi == Anything 
=================================
> As a always, RTFM (read the fucking manual) with anything that you're doing.

> A tablet is a tablet, a phone is a phone, but a Raspberry Pi can become anything you want, used for any task.

![Kindle Keyboard](/imgs/raspberrypi/KindlePiPrj/340px-Amazon_Kindle_3.jpg?raw=true)

>The Amazon Kindle is  a series of e-readers with E Ink electronic paper displays. on July 28, 2010. Amazon announced the third generation Kindle, later renamed "Kindle Keyboard".

>The Kindle is a very low cost, super lightweight, ARM Linux machine with an eInk display that can be easily read in bright sunlight, a great text-to-speech system, amazing battery life,WIFI access, a nice bit of storage, sound output and even a hidden microphone. There are endless creative off-label things you could do with it.

 ：ROOTING  YOUR KINDLE (My Kindle Keyboard)
The first thing we need to do to get control of the device is "jailbreak"(越狱) it. which really just adds a "hacked" key to the keyring used to verify the package signature.

```
Check your Settings page, find what FW your Kindle is running.

Install the Jailbreak [kindle-jailbreak-0.13.N]. To install it you just transfer over the bin that's right for your version of the kindle (I.e., Update_jailbreak_0.13.N_k3w_install.bin = Kindle Keyboard 3 Wifi) into the device root and then update the device: Home > Menu > Settings > Menu > Update Kindle. 

To remove the jailbreak(if you somehow want to get rid of it... There's no practical reason to do this though ;) use the same process described substituting the appropriate "uninstall" bin file.)
```
- [Update_jailbreak_0.13.N_k3w_install.bin](/root/raspberrypi/RaspberryPiPrj/KindlePiPrj/kindle-jailbreak-0.13.N/Update_jailbreak_0.13.N_k3w_install.bin)
- [Update_jailbreak_0.13.N_k3w_uninstall.bin](/root/raspberrypi/RaspberryPiPrj/KindlePiPrj/kindle-jailbreak-0.13.N/Update_jailbreak_0.13.N_k3w_uninstall.bin)

Kindle Screen Saver Hack (the custom ScrrenSavers)
--------------------------------------------------
```
1) Download and unzip the kindle-ss-0.47.N.zip file.
2) Attach your Kindle to a computer using the USB cable.
3) Copy the appropriate ss bin file (for me: Update_ss_0.47.N_k3w_install.bin) to the root of your Kindle
4) Safely eject & unplug your Kindle from your computer. To apply the update, on your Kindle Home screen, click Menu > Settings > Menu > Update Your Kindle.
5) Plug your Kindle to the computer and place your 600x800 image files (png or jpeg) into the "linkss/screensavers" folder. 
6) shuffle your screensavers each time an autoreboot is triggered, drop a blank "shuffle" file in the "linkss" folder. (By copying and renaming the existing "autoreboot" blank file)

To remove the screen saver hack, just copy the appropriate "uninstall" bin file to the root of your Kindle and update. Note that, since the v0.6.N, you shouldn't have to deactivate/uninstall it in order to be able to install official Amazon updates!
```

- [Update_ss_0.47.N_k3w_install.bin](/root/raspberrypi/RaspberryPiPrj/KindlePiPrj/kindle-ss-0.47.N/Update_ss_0.47.N_k3w_install.bin)
- [Update_ss_0.47.N_k3w_uninstall.bin](/root/raspberrypi/RaspberryPiPrj/KindlePiPrj/kindle-ss-0.47.N/Update_ss_0.47.N_k3w_uninstall.bin)

Kindle 3 tricks & hacks 
-----------------------

* Disable my screensaver 
```
holding a page is probably less energy consuming than loading the screensaver! In a few keystrokers, you can disable it and leave the Kindle screen at the latest page that you're reading. 

Now here is the big secret:
    Home screen: (enter)
    ;debugOn (enter)
    ~disableScreensaver (enter)
    ;debugOff (enter) 

There are other hacks from the ;debugOn list, you can list them with the ~help or simply try these (play at your own risk, I only used the ScreenSaver personally):

~changeLocal
~disableIndexing
~disableScreensaver
~dumpIndexStats
~exec
~help
~indexStatus
~meminfo
~reloadContentRoster
~resumeScreensaver
~startindexing
~stopindexing 
~usbNetwork 
```
* Games 
    
    Shift + alt + m = play Minesweeper(from homescreen)
    GoMoku: press G from Minesweeper 

![screen shot game](/imgs/raspberrypi/KindlePiPrj/screen_shot_game.gif?raw=true)

* Hot keys at any time 

    - shift + alt + G = screenshot (plug your kindle in via the USB and navigate to the folder 'documents' screenshots are GIF and named something like "screen_short.***.gif")
    - alt + G = screen refresh 
    - alt + home = Kindle Store 
    - alt + top row of letters on keyboard = numbers 1-0

* Music Controls
    
    - alt + space = turn music on and off 
    - alt + f = skip to next track 

* Kindle 3 Image Viewer 
    
>Kindle has an image viewer. Who knows why its hidden (other than maybe its not very good), but still it's there and simple to set up.
>Plug your Kindle 3 into the computer with the USB. Open the Kindle drive that is now in your displayed with your removable drives
>in the root create a folder called "pictures" within that folder you can create a number of other folders (think of them as collections), then add your images/pictures to this(or these) folders. I've only tried Jpegs and they work find. Once finished safely unplug the kindle 

* Image Viewer Functions 
    
    - Page forward and back to see different images 
    - f = full-screen 
    - q = zoom in 
    - w = zoom out 
    - e = reset zoom 
    - c = actual size 
    - r = rotate 
    - nav controller = pan 

* Restart Your Kindle 
    
    - To restart Kindle keyboard (3rd Generation):
    - 1. Slide and hold the **Power** button for a full 40 seconds. After the first 6 to 8 secons, the screen will go blank, which is normal. Continue holding the Power button.
    - 2. After 40 seconds, release the **Power** button. The charge indicator light will turn on after a few seconds.


Kindle + Raspberry Pi + Logitech K480 = A Portable Outdoor Hackstation
======================================================================

>Using a Kindle as a screen, connecting it to the processing power of the Raspberry Pi while using an external keyboard to work comfortably. Since conecting an extral keyboard to the Kindle seemed impossible at that point. I need to use the raspberry pi as the 'hub'.

Lets get started
----------------
* a Kindle (I use Kindle 3 keyboard wifi)
* a Raspberry Pi (I use Raspberry Pi 3B)
* 2 micro usb to usb cables (one for power and one to connect the Kindle to the Raspberry Pi)
* One keyboard connected to the Raspberry Pi (I use Logitech Bluetooth K480)

![Kindle Raspberry Pi Logitech K480](/imgs/raspberrypi/KindlePiPrj/kindle_raspberry.png?raw=true)

Hacking the Kindle 
------------------

**DISCLAIMER - you can brick (render unusable) your Kindle doing so, these are just pointers and I take no responsibility whatever you do with your kindle, or your like...**

The first part, connecting the Kindle to the Raspberry Pi is simple enough. 
> [Jail break the Kindle](http://wiki.mobileread.com/wiki/Kindle_Hacks_Information#Jail_break_JB)

> Launchpad -- yet another hotkey manager for Kindle, to get the Launchpad software which is required to run the terminal emulator later. Download the file: [lpad-pkg-001d](https://www.mobileread.com/forums/attachment.php?attachmentid=141887&d=1441954643) and unzip. Find the correct install binary for your device. I used: update_launchpad_0.0.1d_k3w_install.bin

> install a [terminal emulator](https://www.mobileread.com/forums/showthread.php?t=154500).
    - Terminal Emulator for Kindle. The terminal emulator is named myts. This is an enhanced version done by Matan based on the original [kiterm](http://info.iet.unipi.it/~luigi/kindle/) by Luigi Rizzo.
    - The latest download link is http://my.svgalib.org/kindle/myts-8.zip
    - After unzipping the archive, you will fond 2 folders: myts and launchpad.
    - mv mytes/ and launchpad to /mnt/us 
    - To make sure that this new ini configuration file is read,safely disconnect the Kindle and issue this hotkey sequence:[Shift][Shift][Space].You should see a command 'Success!' notification on the Kindle when you issue this command.
    - After installing, the default launchpad configuration (in the file /mnt/us/launchpad/myts.I.ini) is :
        [Shift] T A = !/mnt/us/myts/myts.sh kill
        [Shift] T T = !/mnt/us/myts/myts.sh 1
        [Shift] T Y = !/mnt/us/myts/myts.sh 2
        [Shift] T U = !/mnt/us/myts/myts.sh 3
        You can hit the left back arrow (the Kindle's page turning buttons) to exit temporarily.

> install [UsbNetwork](http://www.mobileread.com/forums/showthread.php?t=88004).
> What's usbnet? The Kindle 2 has a hidden USB network mode, probably left over from development. When activated, the Kindle would behave as a USB network device rather than a USB mass storage device. This allowed you to do neat things such as tethering the device to your laptop. Kindle keyboard version seems to have removed this feature, but the usbnet hack reactivates it and installs busybox (a
> micro shell environment), dropbear (a micro SSH server) and a few other utilities to you to SSH into your device and explore its insides.
    - Install the usbnetwork [kindle-usbnetwork-0.57.N-k3](https://www.mobileread.com/forums/attachment.php?attachmentid=141340&d=1440341473). To install it you transfer over the bin that's right for your version of the kindle (I.e.,Update_usbnetwork_0.57.N_k3w_install.bin = Kindle Keyboard 3 Wifi).
    - After installation, usbnet creates a usbnet directory in your kindle root which contains its configuration files:
```
$ tree usbnet -d
usbnet
├── bin
├── empty
├── etc
│   ├── dot.ssh
│   ├── ltrace
│   ├── nano
│   ├── terminfo
│   │   ├── a
│   │   ├── d
│   │   ├── l
│   │   ├── r
│   │   ├── s
│   │   ├── v
│   │   └── x
│   └── zsh
├── lib
│   └── zsh
│       └── net
├── libexec
├── run
├── sbin
└── share
    ├── misc
    └── zsh
        ├── functions
        │   ├── Calendar
        │   ├── Chpwd
        │   ├── Completion
        │   │   ├── AIX
        │   │   ├── BSD
        │   │   ├── Base
        │   │   ├── Cygwin
        │   │   ├── Darwin
        │   │   ├── Debian
        │   │   ├── Linux
        │   │   ├── Mandriva
        │   │   ├── Redhat
        │   │   ├── Solaris
        │   │   ├── Unix
        │   │   ├── X
        │   │   ├── Zsh
        │   │   └── openSUSE
        │   ├── Exceptions
        │   ├── MIME
        │   ├── Misc
        │   ├── Newuser
        │   ├── Prompts
        │   ├── TCP
        │   ├── VCS_Info
        │   │   └── Backends
        │   ├── Zftp
        │   └── Zle
        ├── help
        ├── scripts
        └── site-functions
```
    - Now unmount(I.e.,"eject") the Kindle from our computer, disconnect the USB connection to take it out of mass storage mode and enable usbnet mode. 
    - Press [DEL] on your Kindle to bring up the search bar and do this following "searches":
```
;debugOn
~usbNetwork
;debugOff
```
    - The commands are not case sensitive. Usually you don't want to stay in debugging mode because it turn Off various power savings features such as turning off WiFi is your Kindle is not connected to the USB. Also, It turns on verbose logging. 
    - Now When you connect your Kindle to your Computer via USB, it itn't recognized as a mass storage device but rather as a USB network devices.
    - Note that with the **usbnet** hack, bu default SSH only works over the USB host-to-host conection. SSH is configured not to ask for the root password so usbnet wisely disables SSH over WIFI for security reasons.
    - Now let's login to our Kindle for the first time:

> Make sure the usbNetwork is enable, Connect the devices through USB, do a quick ifconfig usb0 192.168.2.1
![macOS network setting](/imgs/raspberrypi/KindlePiPrj/mac_network_setting.png?raw=true)

> I can login into the Raspberry Pi with no problem. 
![ifconfig usbNetwork](/imgs/raspberrypi/KindlePiPrj/ifconfig_usb.png?raw=true)

> Using the great display of the Kindle but sadly also using it's limiting keyboard 
![kindle terminal](/imgs/raspberrypi/KindlePiPrj/kindle_usb_network.png?raw=true)

> The main challenge now is to use the keyboard connected to the Raspberry Pi instead of the Kindle's. This is where the magic of **GNU SCREEN** comes in play! Screen is a terminal multiplexer, screen is that you can be multiple user on the same screen session.

> So what happen here, is that using the keyboard connected to the Raspberry Pi, you will login into the Raspberry Pi with the Kindle and the share the same screen session so that you can use the keyboard connected on the Raspberry pi.You will still need to use the kindle keyboard to create that first connection, but once your connected, you can use your main keyboard.

**Use network for the Raspberry Pi**

> First we want to be able to use UsbNetworking when connecting Kindle. When the Kindle is on usbNetworking, it assign the ip 192.168.2.2 to its USB port. When then need the Raspberry Pi to assign its USB port the 192.168.2.1 and that has to be automatic. To do so, the first step is to add to your **/etc/network/interfaces**
```
allow-hotplug usb0 
mapping hotplug 
script grep 
map usb0
iface usb0 inet static
address 192.168.2.1
netmask 255.255.255.0
broadcast 192.168.2.255
up iptables -I INPUT 1 -s 192.168.2.1 -j ACCEPT 
```

Install KindleVNC viewer
-----------------------
> A VNC viewer for ebook readers -- https://github.com/hwhw/kindlevncviewer

![kindlevncviewer.zip](/root/raspberrypi/RaspberryPiPrj/KindlePiPrj/kindlevncviewer.zip)
```
Installation/Running:

Copy the fill directory "kindlevncviewer" to the (USB-storage) root of your device.

You'll probably want to use this in combination with the "launchpad" application. A config file for 
launchpad is included. you might need to edit it to your needs. The copy it (it's in the "launchpad"
directory) to the "launchpad" directory on your device, For configuration, consider the following information:

You can connect to VNC servers by two means:

- USB connection:
  You will need to have the USB networking hack running.
  The distributed launch pad config file is configured to start a viewer connection to
  192.168.2.1:1, which is display :1 on the USB networking host if you use
  standard config for USB networking. It will use the key chain "V U" by default,
  so the whole key chain to press is "Shift V U".

- Wifi connection:
  Of course, you must activate Wifi in order to connect.
  The distributed launch pad config will start a connection to
  somewifihost:1, you will most certainly have to edit this to suit your needs.
  The standard key chain is "V W", including the launchpad start key, this
  would be "Shift V W".

The launchpad config will kill a running VNC viewer with the key chain "V Q"
("Shift V Q" is the complete key chain you must press).
```
