Kindle + Raspberry Pi == Anything 
=================================
> As a always, RTFM (read the fucking manual) with anything that you're doing.

> A tablet is a tablet, a phone is a phone, but a Raspberry Pi can become anything you want, used for any task.

![Kindle Keyboard](/imgs/raspberrypi/KindlePiPrj/340px-Amazon_Kindle_3.jpg?raw=true)

>The Amazon Kindle is  a series of e-readers with E Ink electronic paper displays. on July 28, 2010. Amazon announced the third generation Kindle, later renamed "Kindle Keyboard".

>The Kindle is a very low cost, super lightweight, ARM Linux machine with an eInk display that can be easily read in bright sunlight, a great text-to-speech system, amazing battery life,WIFI access, a nice bit of storage, sound output and even a hidden microphone. There are endless creative off-label things you could do with it.

 ：ROOTING  YOUR KINDLE (My Kindle Keyboard)
The first thing we need to do to get control of the device is "jailbreak"(越狱) it. which really just adds a "hacked" key to the keyring used to verify the package signature.

Jailbreak the Kindle
--------------------
> jailbreak the Kindle(don't worry, it's not illegal if it's your property)
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

USBNetwork Hacks for Kindle
---------------------------
> USBNetwork will grant you remote shell access to your Kindle, either over USB or WiFi.
```
> install [UsbNetwork]
> What's usbnet? The Kindle 2 has a hidden USB network mode, probably left over from development. When activated, the Kindle would behave as a USB network device rather than a USB mass storage device. This allowed you to do neat things such as tethering the device to your laptop. Kindle keyboard version seems to have removed this feature, but the usbnet hack reactivates it and installs busybox (a
> micro shell environment), dropbear (a micro SSH server) and a few other utilities to you to SSH into your device and explore its insides.
 - Install the usbnetwork [kindle-usbnetwork-0.57.N-k3](https://www.mobileread.com/forums/attachment.php?attachmentid=141340&d=1440341473). To install it you transfer over the bin that's right for your version of the kindle (I.e.,Update_usbnetwork_0.57.N_k3w_install.bin = Kindle Keyboard 3 Wifi).
- After installation, usbnet creates a usbnet directory in your kindle root which contains its configuration files:

> Configure usbNetWork
    - $ cd usbnet/
    - $ mv DISABLED_auto auto
    - $ cd etc && vim config
        K3_WIFI="true"
        K3_WIFI_SSHD_ONLY="true"

> Create password key 
    - (macOS)
    - $ ssh-keygen -t rsa 
    - $ cat ~/.ssh/id_rsa.pub | pbcopy 
    - (Kindle 3)
    - $ vim usbnet/etc/authorized_keys
        <paste>将👆产生的公钥粘贴并保存文件
    - umount Kine and [Home] -> [Menu] -> Settings -> [MENU] -> Restart

> Check Kindle IP address 
    - [Home] -> [Menu] -> Settings (From Kindle 3 Keyboard) Input alt+u, alt+q, alt+q 
    - Input 711 page

> $ scp something root@192.168.31.158:/mnt/us/documents 

> Kindle documemt Refresh Probelm
    Because copy to (kindle) /mnt/us/documents folder files will not automatically detect, so you need a refresh mechanism, otherwise you will need to restart after each transfer file.
    $ cd /mnt/us/usbnet/
    $ vi refresh_kindle3
        dbus-send --system /default com.lab126.powerd.resuming int32:1
    $ chmod +x refresh_kindl3

NOTE: /mnt/us = USB连接时K3的根目录
```
- [Update_usbnetwork_0.57.N_k3w_install.bin](/root/raspberrypi/RaspberryPiPrj/KindlePiPrj/kindle-usbnetwork-0.57.N-k3/Update_usbnetwork_0.57.N_k3w_install.bin)
- [Update_usbnetwork_0.57.N_k3w_uninstall.bin](/root/raspberrypi/RaspberryPiPrj/KindlePiPrj/kindle-usbnetwork-0.57.N-k3/Update_usbnetwork_0.57.N_k3w_uninstall.bin)
![Kindle 711 page](/imgs/raspberrypi/KindlePiPrj/711.png?raw=true)
![Kindle usbNetwork](/imgs/raspberrypi/KindlePiPrj/usbNetwork_Kindle.png?raw=true)

Launchpad Hacks for Kindle 
--------------------------
>launchpad -- another hotkey manager for Kindle 
```
launchpad for Kindle is a small program supporting extended input capabilities.The main purpose of it is providing the ability to run any 3rd-party programs from within the original unmodified Kindle Framework software. It can be also used to organize custom keyboard shortcut operations and to simplify input of special symbols.

- Install:
    - unpack the attached Ipad-pkg-xxx.zip archive somewhere.
    - select the Kindle update package for your device model[update_launchpad_0.0.1d_k3w_install.bin] and copy it to your device under user root directory [/mnt/us]
    - apply the standard Amazon Kindle update procedure.

- Create launchpad refresh_kindle3 
    - $ cd /mnt/us/launchpad
    - $ cat launchpad.ini 
;;; 
;;; when started, the kindle launchpad just transparently scans keypad and 
;;; fiveway keystrokes until the user presses and releases the hot sequence 
;;; Introducer key. Then the launchpad enters the hotkey mode: it captures 
;;; all system input, engages the interval timer to trigger after specified 
;;; HotInterval milliseconds and starts collecting further keystrokes in an internal 
;;; hotkey sequence buffer. 
;;; When the hotkey interval timer triggers or the Trailer key is pressed, the system
;;; input capture gets released, and an attempt to execute collected hotkey action
;;; is made. Available hotkey actions are controlled by contents of the [Action]
;;; section below   

; Kindle input key symbolic names are used to specify the hotkey sequence introducer
; and trailer keys. See keydefs.ini for details
[Settings]
Introducer = Shift
Trailer = Enter
HotInterval = 700
ScriptDirectory = ./scripts
KeyboardInput = /dev/input/event0
FivewayInput = /dev/input/event1
InterKeyDelay = 300

;;; hotkey actions are defined below as <key_sequence> = <action_command>
;;; one action definition per text line.
;;; 
;;; <key_sequence> is a blank separated list of key symbolic names. See keydefs.ini for details.
;;; <action_command> describes the action to execute on a particular hotkey sequence.
;;; Currently three type of action supported depending on the first character of the 
;;; command string:
;;;  '!' -- shell command. The <action_command> string excluding the leading '!' is sent to the
;;;         system shell, exactly as it was typed from the console.  
;;;  '@' -- Kindle Framework script. The <action_command> string excluding the leading '@' is interpreted
;;;         as a name of a special script containing command information obeying format of
;;;         the known hotkeys package. The main purpose of these scripts is to simplify
;;;         entering special symbols into kindle Framework search box
;;;  '#' -- Kindle Framework key sequence. Similar to the above, but doesn't require 
;;;         external script.
;;;   all other command strings are interpreted as a sequence of a send_key commands. The contents of these 
;;;   commands gets interpreted and sent as a sequence of simulated keystrokes to the input subsystem.
;;;   Such commands consist of the space-separated tokens, which can be symbolic key names and/or
;;;   ascii strings enclosed in quotes (")
;;;
;;;   Note: to correctly accept  kindle key sequence starting with a special
;;;         symbol, the Framework search box should be brought up, if not already.
;;;         Press the 'Del' key on Kindle in order to bring the search box up
;;;
 
[Actions]
;
; hotkey sequence definitions below are provided for reference only.
; uncomment corresponding line(s) and restart the Program in order to enable
; these definitions
;

;Dot = @SHIFT-DOT.sh
;Slash = @SHIFT-SLASH.sh
;;0 = @SHIFT-0.sh
;;1 = @SHIFT-1.sh
;;2 = @SHIFT-2.sh
;;3 = @SHIFT-3.sh
;;4 = @SHIFT-4.sh
;;5 = @SHIFT-5.sh
;;6 = @SHIFT-6.sh
;;7 = @SHIFT-7.sh
;;8 = @SHIFT-8.sh
;;9 = @SHIFT-9.sh
;
;;P = #')'
;;O = #'('
;;I = #'*'
;;U = #'&'
;;Y = #'^'
;;T = #'%'
;;R = #'$'
;;E = #'#'
;;W = #'@'
;;Q = #'!'
;;Dot = #','
;;Slash = #'?'
;
;;D = #';' "debugOn"
;;N = #"`usbNetwork"
;;X = "just a string"
    - $ echo "R F = !/mnt/us/usbnet/refresh_kindle3" >> launchpad.ini 
    (Kindle 3) Shift + R + F to refresh kindle documents
```
- [update_launchpad_0.0.1d_k3w_install.bin](/root/raspberrypi/RaspberryPiPrj/KindlePiPrj/lpad-pkg-001d/update_launchpad_0.0.1d_k3w_install.bin)
- [update_launchpad_0.0.1d_k3w_uninstall.bin](/root/raspberrypi/RaspberryPiPrj/KindlePiPrj/lpad-pkg-001d/update_launchpad_0.0.1d_k3w_uninstall.bin)

Install Python on the Kindle 
----------------------------
```
Copy the appropriate Update_python_0.14.N_k3w_install bin file (for me(Kindle3): Update_python_0.14.N_k3w_install.bin) to the root(/mnt/us) of your Kindle
Safely eject & unplug your Kindle from your computer. To apply the update, on your Kindle Home screen, click Menu > Settings > Menu > Update Your Kindle. 
```
- [Update_python_0.14.N_k3w_install.bin](/root/raspberrypi/RaspberryPiPrj/KindlePiPrj/kindle-python-0.14.N-k3w/Update_python_0.14.N_k3w_install.bin)
- [Update_python_0.14.N_k3w_uninstall.bin](/root/raspberrypi/RaspberryPiPrj/KindlePiPrj/kindle-python-0.14.N-k3w/Update_python_0.14.N_k3w_uninstall.bin)


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

>The first part, connecting the Kindle to the Raspberry Pi is simple enough. 
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

- [kindlevncviewer.zip](/root/raspberrypi/RaspberryPiPrj/KindlePiPrj/kindlevncviewer.zip)

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

Using Kindle as an External Monitor 
-----------------------------------
> You can share a terminal session using your Kindle, which means you can use it as an external monitor for text-only applications. You won't be able to do much web browsing or design work beside ASCII art, but if you're a coder or a sysadmin, I'm sure this is not really to get this to bother you.
```
# Here's a brief list of steps required to get the hack working.
    1. Jailbreak your Kindle 
    2. Install a Terminal application on it so that you can open a ssh/telnet session (Used KindleTermPV).
    3. Disable the screensaver on the Kindle 
    4. Make sure your host computer has ssh/telnet properly setup (and your firewall also)
    5. Configure your Kindle Terminal application to connect automatically to your host computer and spawn a screen session at startup. For KindleTermPV, I create a kindleterm.properties file and placed it /mnt/us/developer/KindleTermPV/work with the following content:
        host 192.168.1.251
        port 22 
        orientation landscape 
        login user_name
        password <pass here>
        cmd screen -m -S shared 
        # Hmm, yeah don't do this over WiFi. USB only!
    6. Open your Kindle Terminal application from your Kindle, which will spawn a screen session. The From your host machine using the same user(user_name), run a "screen -x shared" 

# Now the two sessions are shared and whatever you type on your computer will appear on the Kindle! You could potentially attach multiple Kindle devices and share multiple shell sessions

# Notable Problems:
    1. Console only, no graphics
    2. Artifacts appearing for certain characters, probably due to the terminal encoding.
    Half a second delay between typeing and seeing the screen update (not a problem if you are used to dial-up speeds and use ssh).
    3. Sometimes the Kindle invalidates certain area of the scrren and you can't see some parts of the text (a "clear" comamnd fixes it or a full refresh of the page does it also).
```

Kindle using VNC
----------------
```
# 1. Jailbreak Kindle 
# 2. Activate SSHD over WIFI/USBnet
https://www.youtube.com/redirect?redir_token=qklmnK-Sx6lYkvbzU1p7aSi-8wJ8MTU3MjQ0NjEwOEAxNTcyMzU5NzA4&q=http%3A%2F%2Fblog.joschika.tk%2F2012%2F03%2F01%2Fkindle-4nt-ssh-over-wifi%2F&v=THuLv2IFLW0&event=video_description 
# 3. Install kindlevnc viewer 
https://www.youtube.com/redirect?redir_token=qklmnK-Sx6lYkvbzU1p7aSi-8wJ8MTU3MjQ0NjEwOEAxNTcyMzU5NzA4&q=http%3A%2F%2Fwww.mobileread.com%2Fforums%2Fshowthread.php%3Ft%3D150434&v=THuLv2IFLW0&event=video_description
# 4. Install kite (to launch kindlevnc)
https://www.youtube.com/redirect?redir_token=qklmnK-Sx6lYkvbzU1p7aSi-8wJ8MTU3MjQ0NjEwOEAxNTcyMzU5NzA4&q=http%3A%2F%2Fwww.mobileread.com%2Fforums%2Fshowthread.php%3Ft%3D168270&v=THuLv2IFLW0&event=video_description
# 5. Launch VNC server 
    $ vim .vncserver.sh 
        vncserver :1 -geometry 600x800 -depth 16 -dpi 160 -alwayshared -lazytight 
    $ ./vncserver.sh && sleep 1 && vncserver localhost:1

# 6. ??
# 7. Profit
```

Kindle 3 Keyboard Shortcuts 
-----------------------------
> https://blog.diannegorman.net/2010/09/kindle-3-keyboard-shortcuts-et-al/
```

# Hardware of Kindle 3 keyboard
two slot on the left side of the kindle 3, one near the top and one near the bottom, they are used to attach covers. The bootom slot also supplies the power for the lighted cover.

The bottom hole can be used to attach serial line to Kindle using very simple connector made from a little bit of PCB.
```

Literary Clock Made From Kindle
-------------------------------

* Step 1: Tools and Materials 
    - Kindle 3 WiFi(nicknamed K3, or K3W)
    - computer (any operating system), with SSH client

* Step 2: Jailbreaking the Kindle 
> In order to change the Kindle into a clock, need to get into the system files. In order to do that, need to open it up through a process called 'jailbreaking' (don;t worry, it's not illegal if it's your property).
    - Jailbreaking 
    - Install usbnetwork (grant you remote shell access to your Kindle, either over USB or WiFi)
    - Install Launchpad 
    - Install Python 

* Step 3: Making an Image for Every Single Minute of the Day 
```
There are 1,440 minutes in a day. Compiling a list with quotes for each and every one of them from different literary works is a massiv undertaking. Big relief: other already did that for us. 

In 2011. newspaper The Guardian asked its readers to submit quotes from books which mention times. Unfortunately the list does not cover all minutes of the day. I worked around this by using some quotes more than once, for instance if it can be used both in the AM and PM.

Even with this pleasant list, two things took me an unreasonable amount of time. I needed to turn every single quotation from the list into an image. I wanted to make them fit nicely to the screen, so the font would be large as possible for each quotation. 
```
- [Kindle clock quotes image.zip](/root/raspberrypi/RaspberryPiPrj/KindlePiPrj/images.zip)

* Step 4: Starting and Stopping the Clock 
```
I wanted to be able to start my literary clock by pressing the shortcut Shift + C on the small keyboard of the e-reader. Pressing it again stops the clock and turns the clock into a normal e-reader again.

# First, create this folder:
$ ssh root@192.168.31.158


Welcome to Kindle!

#################################################
#  N O T I C E  *  N O T I C E  *  N O T I C E  # 
#################################################
Rootfs is mounted read-only. Invoke mntroot rw to
switch back to a writable rootfs.
#################################################
[root@kindle root]# cd /mnt/us
[root@kindle us]# ls 
DK_BookStore  DK_Download   DK_Sync       documents     launchpad     music         system
DK_Documents  DK_News       audible       extensions    linkjail      python        usbnet
[root@kindle us]# mkdir timelit     # create this folder 
[root@kindle us]# ls && cd timelit
DK_BookStore  DK_Download   DK_Sync       documents     launchpad     music         system        usbnet
DK_Documents  DK_News       audible       extensions    linkjail      python        timelit
[root@kindle timelit]# scp -r chyiyaqing@192.168.31.209:~/Downloads/timelit/* .
Password:
clockisticking                                                                                     100%   42     0.0KB/s   00:00    
showMetadata.sh                                                                                    100%  531     0.5KB/s   00:00    
startstopClock.sh                                                                                  100%  833     0.8KB/s   00:00    
timelit.sh                                                                                         100%  892     0.9KB/s   00:00    
[root@kindle timelit]# 
[root@kindle timelit]# scp -r chyiyaqing@192.168.31.209:~/Downloads/images .   # Copy images 
[root@kindle timelit]# ls
clockisticking     images             showMetadata.sh    startstopClock.sh  timelit.sh
[root@kindle launchpad]# cd /mnt/us/launchpad && vi startClock.ini  # put this text in there 
    [Actions]
    C = !sh /mnt/us/timelit/startstopClock.sh &

That creates the shortcut Shift + C.(Note, one key for one key input) If we press that, the bash-script startstopClock.sh starts. It stops the Kindle framework (the normal user interface), prevents the Kindle from going into power save mode and creates a small file(/mnt/us/timelit/clocksticking) to indicate the clock has started.

If the user presses Shift+C again and the clockisticking file is already there, startstopClock.sh will remove it and restart the Kindle. 

startstopClock.sh also executes another script, showMetadata.sh, to enable the keystrokes that will show the metadata (using the command /usr/bin/waitforkey). If the user pushes the "next page" button on the sides of the Kindle. it will check if the clock is ticking and if it is. will show the same image as currencly is shown (which file that is, is saved in the clockisticking file) but then with title and author at the bottom.

Changing the time on the display every minute is done by adding this line to /etc/crontab/root
# If you see like this Error root: Read-only file system
$ mntroot rw 
$ vi /etc/crontab/root 
    * * * * * sh /mnt/us/timelit/timelit.sh 
# restart crontab
$ /etc/init.d/cron restart 

Every time it is run, timelit.sh checks if the 'clocksticking' file is created. If it is. timelit.sh proceeds to show the image for the current minute. 

Note: You'll probably want to change the timezone in timelit.sh 'TZ='
```
- [Kindle clock quotes timelit.zip](/root/raspberrypi/RaspberryPiPrj/KindlePiPrj/timelit.zip)
