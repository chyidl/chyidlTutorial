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


Kindle + Raspberry Pi + Logitech K480 = A Portable Outdoor Hackstation
======================================================================

http://ponnuki.net/2012/09/kindleberry-pi/
