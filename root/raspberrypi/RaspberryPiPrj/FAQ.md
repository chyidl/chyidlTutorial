# FAQs
======

## Table of contents

### What is a Raspberry Pi?

Raspberry Pi is the third best-selling computer brand in the world. The Raspberry Pi is a credit-sized computer that plugs into your TV or display, and a keyboard and mouse. You can use it to learn coding and to build electronics projects, and for many of the things that you desktop PC does,like spreadsheets, word processing, browsing the internet, and playing games. It also plays high-definition video. The Raspberry Pi is being used by adults and chirldren all over the
world to learn programming and digital making.

## The computer hardware 

### What are the differences between Raspberry Pi models?

| Product   | SoC   | Speed     | RAM   | GPU       | Storage   | USB Ports | Ethernet  | Wireless/Bluetooth    | HDMI | Power input |
|:--------- |:----- |:--------- |:----- |:--------- |:----------|:----------|:--------- |:----------------------|:-----|:------------|
|Raspberry Pi 2 Model B|BCM2836, quad-core Cortex-A7|900MHz|1GB LPDDR2 SDRAM|Broadcom VideoCore VI|microSD card storage|4 USB 2 ports|100 Base Ethernet|No|Full-size HDMI|5V/2.5A DC power input||
|Raspberry Pi 3 Model B|BCM2837,Cortex-A53(ARMv8)64|1200MHz|1GB LPDDR2 SDRAM|Broadcom VideoCore VI|microSD card storage|4 USB 2 ports|100 Base Ethernet|BCM43438 wireless LAN and Bluetooth Low Energy (BLE) on board|Full size HDMI| 5V/2.5A DC power input|
|Raspberry Pi 3 Model B+|BCM2837B0, Cortex-A53(ARMv8)64-bit SoC|1400MHz|1GB LPDDR2 SDRAM|Broadcom VideoCore VI|microSD card storage|4 USB 2.0 ports|Gigabit Ethernet over USB 2.0(maximum throughput 300 Mbps)|2.4GHz and 5GHz IEEE 802.11.b/g/n/ac wireless LAN, Bluetooth 4.2, BLE|Full-size HDMI|5V/2.5A DC power input|
|Raspberry Pi 4 Model B|BCM2711,Quad core Cortex-A72 (ARM v8)64-bit SoC|15000MHz|1GB,2GB or 4GB LPDDR4-2400 SDRAM|Broacom VideoCore VI|microSD card storage|2 USB 3.0 ports; 2 USB 2.0 ports|Gigabit Ethernet|2.4GHz and 5.0 GHz IEEE 802.11ac wireless, Bluetooth 5.0, BLE|2 x micro-HDMI ports(up to 4kp60 supprted)|5V DC/3A|
|Jetson Nano|Quad core Cortex-A57 SoC|14300MHz|4GB LPDDR4-2400 SDRAM|128 CUDA core Maxwell|microSD card storage|4 x USB 3.0|Gigabit Ethernet(& E-keyed M.2)|1xHDMI & 1xDP up to 4K, 60fps, H.264 & H.265 hardware decoding up to 4K at up 60fps|Micro USB or barrel jack|

In February 2015, Raspberry Pi 2 Model B, the second generation of the Raspberry Pi. The Pi 2 shares many specs with the Pi 1 B+, and originally used a 900MHz quad-core ARM Cortex-A7 CPU and has 1GB RAM. Some recent version of the Pi 2(v1.2) now use a 900MHz ARM Cortext-A53 CPU.

The Pi 3 Model B was launched in February 2016. It uses a 1.2GHz 64-bit quad-core ARM Cortex-A53 CPU, has 1GB RAM, integrated 802.11n wireless LAN, and Bluetooth 4.1.

The Pi 3 Model B+ was launched in March 2018. It uses a 1.4GHz 64-bit quad-core ARM Cortext-A53 CPU, has 1GB RAM, gigabit Ethernet, integrated 802.11ac/n wireless LAN, and Bluetooth 4.2.

### What hardware interfaces does it have?

Depending on the model, the Raspberry Pi has either 40 or 26 dedicated interface pins. In all cases, these include a UART, an I2C bus, a SPI bus with two chip selects, I2S audio, 3v3,5v,and ground. The maximum number of GPIOs can theoretically be indefinitely expanded by making use of the I2C or SPI bus. CSI-2 camera port for the Raspberry Pi Camera Modele, and a DSI display port for the Raspberry Pi LCD touchscreen display. CSI-2 camera port for the Raspberry Pi Camera Modele, and a DSI
display port for the Raspberry Pi LCD touchscreen display.

## Performance 

### How powerful is it?

The GPU provides OpenGL ES 2.0, hardware-accelerated OpenVG, and 1080p30 H.264 high-profile encode and decode. The GPU is capable of 1GPixel/s, 1.5Gtexel/s or 24 GFLOPs of general purpose compute and features a bunch of texture filtering and DMA infrastructure. This mean that graphics capabilities are roughly equivalent to the original Xbox's level of performance. Overall read-world performance for Models A,A+,B,B+,CM,Zero and Zero W is something like a 300MHz Pentium 2, only with much
better graphics. The Pi 2 Model B is approximately equivalent to an Athlon Thunderbird running at 1.1GHz: agin, it has the much hihgher-quality graphics that come frome using the same GPU as in previous models. The Pi 3 Model B is around twices as fast as Pi 2 Model B, depending on the benchmarks chosen.

### Why does my Pi run at a slower clock speed that advertised?

The Raspberry Pi(all models) idles at a lower speed than advertised. If the workload of the CPU increases, then the clock speed increases until it reaches its maximum value,which varies between models. If the CPU starts to overhear, there are added complexities: depending on the model,when the device reaches a particular temperature, the clock is throttled back to prevent overheating. This is called termal throttling. If the Pi does thermal-throttle, you will see a warning icon in
the top right corner of the desktop.

### What is its operating temperature? Does it need a heatsink?

The Raspberry Pi is built from commerical chips which are qualified to different temperature ranges; the LAN9514(LAN9512 on older models with 2 USB ports) is specified by the manufacturers as being qualified from 0C to 70C, while the SoC is qualified from -40C to 85C. 

### Why does cpuinfo report I have a BCM2835?

The upstream Linux kernel developers had decided that all models of Raspberry Pi return bcm2835 as the SoC name. At Raspberry Pi we like the use as much upstream kernel code as possible, as it makes software maintenance much easier, so we use this code. Unfortuately it means that cat /proc/cpuinfo is inaccurate for the Raspberry Pi 2 and Raspberry Pi 3, which use the bcm2836 and bcm2837 respectivity. You can use cat /proc/device-tree/model to get an accurate description of the SoC on your
Pi model.

### How do I run a program at startup?

In order to have a command or program run when the Pi boots, you can add commands to the rc.local file. This is especially useful if you want to be able to plug your Pi in to power headless,and have it run a program without configuration or a manual start.
An alternative for scheduled task management is cron.
On your Pi,edit the file /etc/rc.local using the editor of your choice. You must edit with root,for example: 
```
sudo vim /etc/rc.local
```
Add commands below the comment,but leave the line **exit @** at the end, then save the file and exit.
If your command runs continuously (perhaps runs an infinite loop) or is likely not to exit, you must be sure to fork the process by adding an ampersand to the end of the command, like so:
```
python3 /home/pi/myscript.py &
```
Otherwise, the script will not end and the Pi will not boot. The ampersand allows the command to run in a separate process and continue booting with the process running.Also,be sure to reference absolute filenames rather than relative to your home folder.
```
If you /etc/rc.local not running at boot? you may need login and run
$ sudo raspi-config 
Choose "Boot Options" -> "Wait for Network at Boot"->"Yes"
then reboot Pi
$ sudo reboot 
Because the script may need network ready.
```
**Cron** is a tool for configuring scheduled tasks on Unix systems. It is used to schedule commands or scripts to run periodically and at fixed intervals.
**crontab** (cron table) is used to edit the list of scheduled tasks in operation, and is done on a per-user basis; each user (including root) has their own **crontab**
```
# Editing crontab 
$ crontab -e 
# Select an editor
# Add a scheduled task 
# The layout for a cron entry is made up of six components:minute,hour,day of month, month of year,day of week,and the command to be executed.
# m h dom mon dow command 

# View scheduled tasks 
$ crontab -l 

# Run a task on reboot:To run a command every time the Raspberry Pi starts up,
@reboot python /home/pi/myscript.py # This will run your Python script every time the Raspberry pi reboots.
```

### How to set up swap space?

Raspbian uses dphys-swapfile, which is a swap-file based solution instead of the "standard" swap-partition based solution. It is much easier to change the size of the swap
```
# The configuration file is:
$ sudo vim /etc/dphys-swapfile 
# The content is very simple. By default Raspbian has 100MB of swap
CONF_SWAPSIZE=1024
# if you want to change the size, you need to modify the number and restart dphys-swapfile:
$ sudo /etc/init.d/dphys-swapfile restart 
# On Raspbian the default location is /var/swap, which is (of course) located on the SD card.
```

## Video 

### What codecs can it play?

The Raspberry Pi can encode (record) and decode(play) H.264(MP4/MKV) out of the box. There are also two additional codecs you can purchase through our Swag Store that enable you to decode MPEG-2, a very popular and widely used format to encode DVDs,video camera recording, TV and many others,and VC-1, a Microsoft format found in Blu-ray discs, Windows Media, Slingbox,and HD-DVDs.

## Audio 

### What about standard audio in and out?

There is standard 3.5mm jack for audio out to an amplifier (not on Zero models).You can add any supported USB microphone for audio in or,using the I2S interface, you can add a codec for additional audio I/O.


## Power 

### Is it safe to just pull the power?

No, not really - you may corrupt your SD card if you do that. We recommend issuing the *sudo halt* or *sudo shutdown* command prior to pulling the power. This ensures that any outstanding file transactions are written to the SD card, and that the SD card is no longer 'active'. Pulling the power during a SD card transaction can occasionally corrupt the card.

### What are the power requirements?

The device is powered by 5V micro USB. Exactly how much current (mA) the Raspberry Pi requires is dependent on which model you are using,and what you hook up to it. We recommend a 2.5A(2500mA) power supply,from a reputable retailer,taht will provide you with enough power to run your Raspberry Pi for most applications,including use of 4USB ports. Very high-demand USB devices may however require the use of a powered hub. The table below outlines the specific power
requirements of each model.

| Product   | Recomended PSU current capacity | Maximum total USB peripheral current draw| Typical bare-board active current consumption |
|:--------- |:------------------------------- |:---------------------------------------- |:--------------------------------------------- |
|Raspberry Pi 2 Model B| 1.8A | 600mA/1.2A(switchable) | 350mA|
|Raspberry Pi 3 Model B| 2.5A | 1.2A | 400mA|
|Raspberry Pi 3 Model B+| 2.5A | 1.2A | 500mA|

### How to fix 'Structure Needs Cleaning' Error 

![Raspberry Pi 3B Ubuntu](/imgs/raspberrypi/StructureNeedsCleaning.png?raw=True)
```
/usr/src/linux-raspi2-headers-4.15.0-1038: Structure needs cleaning Error

# First, Unmount this drive(this is my Raspberry Pi SD Card partition, so I shutdown system and remove sd card) 
# Second, Using SD Card Reader insert another Linux OS. execute below command.
$ sudo fdisk -l # check device 
$ sudo fsck /dev/<unmounted_partition>
```

### Performance benchmark 
```
https://chromium.github.io/octane/
Octane 2.0 is a performace benchmark which were running in chromium 
iMac 2017"21.5 4K       : 47410 
macbook pro 2015"13     : 26352
ipad pro 9.7            : 20947
Raspberry Pi 4B         : 8220 
Jetson Nano             : 7474
Raspberry Pi 3B+        : 2967 
Raspberry Pi 3B         : 2672
```

### Data Transfer 
```
test USB data tranfer speed and the speed of reading a board by micro SD card.
    connect a USB 3 SSD 

# test the speed in the USB interface read performance test of the connected SSD with no caching 
# SanDisk Ultra microSDHC A1, Class 10, U1
$ sudo hdparm -t --direct /dev/sda1 
    Raspberry Pi 3B     :    Timing O_DIRECT disk reads: 86 MB in 3.02 seconds = 28.43 MB/sec 
    Raspberry Pi 3B+    :    Timing O_DIRECT disk reads: 86 MB in 3.02 seconds = 28.29 MB/sec 
    Raspberry Pi 4B     :    Timing O_DIRECT disk reads: 796 MB in 3.00 seconds = 265.18 MB/sec 
    Jetson Nano         :    Timing O_DIRECT disk reads: 866 MB in 3.00 seconds = 288.35 MB/sec 
    
$ sudo hdparm -t --direct /dev/mmcblk0p2 
    Raspberry Pi 3B     :    Timing O_DIRECT disk reads: 66 MB in 3.04 seconds = 21.72 MB/sec 
    Raspberry Pi 3B+    :    Timing O_DIRECT disk reads: 68 MB in 3.08 seconds = 22.06 MB/sec 
    Raspberry Pi 4B     :    Timing O_DIRECT disk reads: 128 MB in 3.04 seconds = 40.77 MB/sec 
    Jetson Nano         :    Timing O_DIRECT disk reads: 188 MB in 3.01 seconds = 62.52 MB/sec 
```
