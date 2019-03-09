Kindle + Raspberry Pi == Anything 
=================================

![Kindle Keyboard](/imgs/raspberrypi/KindlePiPrj/340px-Amazon_Kindle_3.jpg?raw=true)

The Amazon Kindle is  a series of e-readers with E Ink electronic paper displays. on July 28, 2010. Amazon announced the third generation Kindle, later renamed "Kindle Keyboard".

The Kindle is a very low cost, super lightweight, ARM Linux machine with an eInk display that can be easily read in bright sunlight, a great text-to-speech system, amazing battery life,WIFI access, a nice bit of storage, sound output and even a hidden microphone. There are endless creative off-label things you could do with it.

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

    shift + alt + G = screenshot (plug your kindle in via the USB and navigate to the folder 'documents' screenshots are GIF and named something like "screen_short.***.gif")
    alt + G = screen refresh 
    alt + home = Kindle Store 
    alt + top row of letters on keyboard = numbers 1-0

* Music Controls
    
    alt + space = turn music on and off 
    alt + f = skip to next track 

* Kindle 3 Image Viewer 
    
    Kindle has an image viewer. Who knows why its hidden (other than maybe its not very good), but still it's there and simple to set up.
    Plug your Kindle 3 into the computer with the USB. Open the Kindle drive that is now in your displayed with your removable drives, 
    in the root create a folder called "pictures" within that folder you can create a number of other folders (think of them as collections), then add your images/pictures to this(or these) folders. I've only tried Jpegs and they work find. Once finished safely unplug the kindle 

* Image Viewer Functions 
    
    Page forward and back to see different images 
    f = full-screen 
    q = zoom in 
    w = zoom out 
    e = reset zoom 
    c = actual size 
    r = rotate 
    nav controller = pan 



Kindle + Raspberry Pi + Logitech K480 = A Portable Outdoor Hackstation
======================================================================

Using a Kindle as a screen, connecting it to the processing power of the Raspberry Pi while using an external keyboard to work comfortably. Since conecting an extral keyboard to the Kindle seemed impossible at that point. I need to use the raspberry pi as the 'hub'.

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

The first part, connecting the Kindle to the Raspberry Pi is simple enough. **Jail break the Kindle**, install a terminal enulator like. 
