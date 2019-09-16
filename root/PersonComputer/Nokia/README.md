Nokia N900
==========
> The N900 is the first Maemo device which may also be used as  aphone. Its default operating system, Maemo 5, is a Linux-based OS originally developed for Nokia 770 Internet Tablet. It is the first Nokia device based Upon the Texas Instruments OMAP3 microprocessor with the ARM Cortex-A8 core.
```
Manufacturer    :   Nokia
Type            :   Mobile Internet device, handheld computer and smartphone
Release date    :   11 November 2009
Media           :   microSD/microSDHC card[1]
Operating 
system          :   Maemo 5[2] Fremantle on Linux 2.6
CPU             :   TI OMAP 3430 SoC
                    600 MHz ARM Cortex-A8 CPU
                    430 MHz C64x+ DSP[2]
Memory          :   256 MB Mobile DDR
                    768 MB swap space for a total of 1 GB virtual memory[2]
Storage         :   256 MB NAND flash
                    32 GB eMMC flash[2]
Display         :   TFT 800 × 480 resolution
                    89 mm (3.5 in) diagonally
                    105 pixels/cm, 267 ppi[2]
Graphics        :   PowerVR SGX530 GPU supporting OpenGL ES 2.0[2]
Sound           :   Stereo loudspeaker
                    3.5 mm TRRS for Audio/Headphones/Video out
Input           :   Resistive touchscreen
                    Localized backlit keyboard with variations for English, Italian, French, German, Russian, Scandinavian and Spanish
                    microphone
                    3-axis accelerometer
                    Proximity sensor
                    Ambient light sensor
Camera          :   5.0 MP (2,584×1,938) 1/2.5" sensor,[3] f/2.8 5.2mm (31.2mm focal length in 35mm terminology) Carl Zeiss Tessar lens (rear camera)
                    0.3 MP (640×480) f/2.8 (front camera)[2][4]
Connectivity    :   GSM 850/900/1800/1900
                    GPRS 107/64 kbit/s DL/UL
                    EDGE 296/178 kbit/s DL/UL
                    UMTS 900/1700/2100
                    WCDMA 384/384 kbit/s DL/UL
                    HSPA 10/2 Mbit/s DL/UL
                    WLAN IEEE 802.11 b/g
                    Bluetooth 2.1
                    Integrated GPS with A-GPS[1]
                    88-108 MHz FM receiver
                    88-110 MHz FM transmitter
                    Infrared transmitter
Power           :   BL-5J 1320 mAh battery[2]
                    MicroUSB Battery Charger,
Online          :   services Skype, IM chats, Facebook
Dimensions      :   110.9 mm (4.37 in) (h)
                    59.8 mm (2.35 in) (w)
                    18 mm (0.71 in) (d)
                    19.55 mm at thickest part[2]
Mass            :   approx. 181 g (0.399 lb)[2]
Predecessor     :   Nokia N810
                    Nokia N97
Successor       :   Nokia N9
                    Nokia N950 (Limited release, non-retail)
```

Install u-boot from pali
------------------------
> Das U-Boot is bootloader which can boot kernel image with initrd. It can be used for booting more kernels (Nokia stock, kernel-power,...) or for booting other systems (Nemo, Nitdroid, Kubuntu, Debian,...).
> This U-Boot version is new and has nice Bootmenu (like Fanoush Bootmenu or Multiboot packages).
```
Install u-boot from pali on the n900 in Maemo. If this does not work from the graphical interface you may run "apt-get u-boot-flasher" in maemo terminal.
$ apt-get install u-boot-flasher 
```

Installing postmarketOS on the Nokia N900
-----------------------------------------
> PostmarketOS is a touch-optimized, preconfigured AIpine Linux distro for your phone. With support for mainline kernels, this distro may very well become the last OS actively maintained on the N900.
```
Installation:
    Requirements:
        You must use a GNU/Linux distro. 
        At least an 8GB microSD card 
        Python 3.4+ and git 
        Nokia N900 with pali's uboot preinstalled 

    Initialization:
        First initialize pmbootstrap for building.
        Sophisticated chroot/build/flash tool to develop and install postmarketOS.
        $ git clone https://github.com/postmarketOS/pmbootstrap.git
        $ cd pmbootstrap 
        $ ./pmbootstrap.py init  # Init pmbootstrap 
        (if happen ERROR:
        [00:46:40] ERROR: We have split the aports repository from the pmbootstrap repository (#383). Please run 'pmbootstrap init' again to clone it.
        can try remove ~/.config/pmbootstrap.cfg and the running pmbootstrap again, then leave the default workdir
        )
        [15:21:53] Location of the 'work' path. Multiple chroots (native, device arch, device rootfs) will be created in there.
        [15:21:53] Work path [/home/pi/postmarketOS/var/pmbootstrap]: /home/pi/Downloads/postmarketOS/pmbootstrap
        [15:22:27] pmbootstrap does everything in Alpine Linux chroots, so your host system does not get modified. In order to work with these chroots, pmbootstrap calls 'sudo' internally. To see the commands it runs, you can run 'pmbootstrap log' in a second terminal.
        [15:22:27] Setting up the native chroot and cloning the package build recipes (pmaports)...
        [15:22:29] Update package index for aarch64 (4 file(s))
        [17:48:14] Available (155): amazon-thor, asus-duma, asus-flo, asus-grouper, asus-me176c, asus-t00f, asus-tf101, asus-z00t, asus-z00vd, bq-chaozu, chuwi-hi10plus, fairphone-fp1, fairphone-fp2, google-crosshatch, google-glass, gp-peak, htc-a5ul, htc-ace, htc-bravo, htc-evita, htc-flounder, htc-k2ul, htc-m7, htc-m8, htc-protou, htc-ville, htc-vision, htc-vivo, huawei-angler, huawei-cameron, huawei-lua-u22, huawei-y530, infocus-flatfish, jolla-sbj, leeco-s2, lenovo-karate, lg-bullhead,
        lg-d285, lg-d722, lg-d855, lg-dory, lg-e610, lg-h815, lg-hammerhead, lg-lenok, lg-mako, lg-p700, lg-vee7e, lg-w5, meizu-turbo, motorola-athene, motorola-cedric, motorola-falcon, motorola-ghost, motorola-harpia, motorola-lux, motorola-maserati, motorola-montana, motorola-osprey, motorola-peregrine, motorola-potter, motorola-shamu, motorola-surnia, motorola-titan, nextbit-robin, nokia-frt, nokia-n9, nokia-n900, nokia-rm885, oneplus-bacon, oneplus-oneplus2, oneplus-onyx,
        oppo-find-7a, ouya-ouya, pine-a64lts, pine-dontbeevil, pine-pinephone, pine-pinetab, planet-geminipda, purism-librem5dev, qemu-aarch64, qemu-amd64, qemu-vexpress, raspberry-pi, raspberry-pi0, raspberry-pi3, samsung-a3ulte, samsung-a5ulte, samsung-a5y17lte, samsung-apexq, samsung-ariesve, samsung-espresso10, samsung-gts210velte, samsung-gts210vewifi, samsung-hero2lte, samsung-herolte, samsung-i747m, samsung-i8190, samsung-i8200, samsung-i9003, samsung-i9070,
        samsung-i9100, samsung-i9195, samsung-i927, samsung-i9305, samsung-j1mini3g, samsung-jflte, samsung-klte, samsung-kminilte, samsung-kylepro, samsung-kylessopen, samsung-kylevess, samsung-lt01wifi, samsung-lt023g, samsung-maguro, samsung-manta, samsung-matissewifi, samsung-n5110, samsung-n7100, samsung-p4wifi, samsung-s6500d, samsung-serranodsdd, samsung-zanin, semc-anzu, semc-smultron, sony-amami, sony-aries, sony-castor-windy, sony-coconut, sony-honami, sony-nicki,
        sony-scorpion, sony-seagull, sony-sirius, sony-suzu, sony-taoshan, sony-tulip, sony-yuga, surftab-wintron7.0, t2m-flame, tablet-x64uefi, teclast-x80pro, wiko-lenny3, wileyfox-crackling, wingtech-wt88047, xiaomi-aries, xiaomi-armani, xiaomi-cancro, xiaomi-ido, xiaomi-kenzo, xiaomi-mido, xiaomi-santoni, xiaomi-tissot, zte-kis3, zte-p731a20
        [17:48:14] Device [samsung-i9100]:
        [16:28:44] This device has proprietary components, which trade some of your freedom with making more peripherals work.
        [16:28:44] We would like to offer full functionality without hurting your freedom, but this is currently not possible for your device.
        [16:28:44] device-nokia-n900-nonfree-firmware: Wifi firmware
        [16:28:44] Enable this package? (y/n) [y]: y
        [16:30:20] Available keymaps for device (3): us/rx51_us, ch/rx51_ch, it/rx51_it
        [16:30:20] Keymap [us/rx51_us]:
        [17:49:33] Available user interfaces (12):
        [17:49:33] * none: No graphical environment
        [17:49:33] * hildon: (X11) Lightweight GTK+2 UI (optimized for single-touch touchscreens)
        [17:49:33] * i3wm: (X11) Tiling WM (keyboard required)
        [17:49:33] * kodi: (Wayland) 10-foot UI useful on TV's
        [17:49:33] * matchbox: (X11) Very basic user interface for handhelds
        [17:49:33] * mate: (X11) MATE Desktop Environment, fork of GNOME2 (stylus recommended)
        [17:49:33] * phosh: (Wayland) Mobile UI developed for the Librem 5 (aarch64, x86 and x86_64 only for now)
        [17:49:33] * plasma-mobile: (Wayland) Mobile variant of KDE Plasma, optimized for touchscreen (slow without hardware acceleration!)
        [17:49:33] * plasma-mobile-extras: Plasma Mobile with more apps pre-installed (video and music players, pdf reader, etc.)
        [17:49:33] * shelli: Plain console with touchscreen gesture support
        [17:49:33] * sway: (Wayland) Tiling WM, drop-in replacement for i3wm (DOES NOT RUN WITHOUT HW ACCELERATION!)
        [17:49:33] * weston: (Wayland) Reference compositor (demo, not a phone interface)
        [17:49:33] * xfce4: (X11) Lightweight GTK+2 desktop (stylus recommended)
        [17:49:33] User interface [weston]:

    Installation:
        # Start the build process and install the completed image to a sdcard
        $ ./pmbootstrap.py install
* WARNING: loadkmap is already starting
[22:06:39] *** (3/5) PREPARE INSTALL BLOCKDEVICE ***
[22:06:40] (native) create nokia-n900.img (854M)
[22:06:40] (native) mount /dev/install (nokia-n900.img)
[22:06:40] (native) partition /dev/install (boot: 54M, root: the rest)
[22:06:40] (native) format /dev/installp2
[22:06:40] (native) mount /dev/installp2 to /mnt/install
[22:06:41] (native) format /dev/installp1 (boot, ext2), mount to /mnt/install/boot
[22:06:41] *** (4/5) FILL INSTALL BLOCKDEVICE ***
[22:06:41] (native) copy rootfs_nokia-n900 to /mnt/install/
[22:06:52] *** (5/5) FLASHING TO DEVICE ***
[22:06:52] Run the following to flash your installation to the target device:
[22:06:52] * pmbootstrap flasher flash_rootfs
[22:06:52]   Flashes the generated rootfs image to your device:
[22:06:52]   /home/chyi/.local/var/pmbootstrap/chroot_native/home/pmos/rootfs/nokia-n900.img
[22:06:52]   (NOTE: This file has a partition table, which contains /boot and / subpartitions. That way we don't need to change the partition layout on your device.)
[22:06:52] * pmbootstrap flasher flash_kernel
[22:06:52]   Flashes the kernel + initramfs to your device:
[22:06:52]   /home/chyi/.local/var/pmbootstrap/chroot_rootfs_nokia-n900/boot
[22:06:52] * If the above steps do not work, you can also create symlinks to the generated files with 'pmbootstrap export' and flash outside of pmbootstrap.
[22:06:52] NOTE: chroot is still active (use 'pmbootstrap shutdown' as necessary)
[22:06:52] Done 
        $ ./pmbootstrap shutdown 
        $ cd /home/chyi/.local/var/pmbootstrap/chroot_native/home/pmos/rootfs && ls 
        nokia-n900.img 

    Writing an image to the SD card(macOS)
        $ diskutil list  # Identify the disk (not the partition) of your SD card, e.g. disk3, not disk3s1.
        $ diskutil unmountDisk /dev/disk3  # Unmount your SD card by using the disk identifier, to prepare it for copying data:
        $ sudo dd bs=1m if=image.img of=/dev/disk3 conv=sync  # Copy the data to your SD card 
    
    Manually resizing the SD card on Linux
        1. The best way to discover the storage devices connected to your computer is the lsblk command. Here is the sample output:
            $  lsblk 
                NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
                sda           8:0    1   7.3G  0 disk   -- 
                ├─sda1        8:1    1  50.5M  0 part
                └─sda2        8:2    1 802.5M  0 part
                mmcblk0     179:0    0  29.8G  0 disk
                ├─mmcblk0p1 179:1    0   256M  0 part /boot/firmware
                └─mmcblk0p2 179:2    0  29.6G  0 part /
            In this above output, the mmcblk0 is the computer's internal SD card, and the sda device is an SD card that has been inserted into the computer's SD card reader. 
        2. Backup: If you have any data other than a fresh image on the SD card, backup your SD card before resizing partitions. 
            $ sudo fdisk -l /dev/sda  # find out the block size of your sd card first
                Disk /dev/sda: 7.3 GiB, 7822376960 bytes, 15278080 sectors
                Units: sectors of 1 * 512 = 512 bytes
                Sector size (logical/physical): 512 bytes / 512 bytes
                I/O size (minimum/optimal): 512 bytes / 512 bytes
                Disklabel type: dos
                Disk identifier: 0x6bb7e403

                Device     Boot  Start     End Sectors   Size Id Type
                /dev/sda1  *      2048  105468  103421  50.5M 83 Linux
                /dev/sda2       105469 1748991 1643523 802.5M 83 Linux
            Now, look at this line from the output of the previous command. It will determine what we should use as the bs (block size):
                Units: sectors of 1 * 512 = 512 bytes
            So, bs=512 would be the proper syntax in this instance. Other examples could be: bs=2MB(for block size = 2 Megabytes), or bs=4MB (for block size = 4 Megabytes), without specification, dd/dcfldd default to the bytes values.
            $ sudo dd if=/dev/sda of=$HOME/sdbackup.img bs=512 
        
        Resizing:
            With the SD card in your computer or card reader, make sure it's unmounted. Use the correct device designation. In this example. I use sda but your may differ:
            $ sudo umount /dev/sda
            Use the parted (partition editor) tool to resize the partitions. 
            Use parted to examine the card:
            $ sudo parted /dev/sda 
                GNU Parted 3.2
                Using /dev/sda
                Welcome to GNU Parted! Type 'help' to view a list of commands.
                (parted) unit chs
                (parted) print
                Model: Generic- SD/MMC (scsi)
                Disk /dev/sda: 951,4,12
                Sector size (logical/physical): 512B/512B
                BIOS cylinder,head,sector geometry: 951,255,63.  Each cylinder is 8225kB.
                Partition Table: msdos
                Disk Flags:

                Number  Start    End         Type     File system  Flags
                 1      0,32,32  6,144,6     primary  ext2         boot
                 2      6,144,7  108,221,48  primary  ext4
            Nothing uses the card from end of 'cylinder' 108 to the card's maximum at 951.
            Partition 1 is the boot partition. Leave that one alone, Partition 2 is the root partition, which can afford to grow to fill most of the card. If your distribution has a Partition 3 for swap space, then you need to move that to the end of the card. 

        Swap:
            To move the swap partition(if it exists between your root partition and the end of your SD card), first calculate how many cylinders your swap partition needs to move. To calculate the number to use: (Maximum - (Partition 3 End - Partition 3 Start) - 1) = Partition 3 New Start.
            ... 

        Expand the partition:
            To grow the root partition, you must first remove the partition boundaries, then recreate the partition as a larger container, and then resize the file system.As scary as that sounds, it doesn't destroy data, it just redefines the area "around" that data. Even so, you should make sure that you backup any important data before attempting this!
            To remove and then recreate your root partition, assuming that your root partition is numbered 2 (it may not be, if you have a swap partition in the 2 slot, so use print in parted to double check):

                (parted) rm 2
                (parted) mkpart primary 6,144,7 950,221,48
                Warning: The resulting partition is not properly aligned for best performance.
                Ignore/Cancel? Ignore
                (parted) quit
                Information: You may need to update /etc/fstab.
            In this example, the starting address of the new partition is identical to its original value, and the ending address is the end of the SD card. 

        Clean and grow the file system:
            Now that you have room for a bigger file system, you must clean and then grow the existing file system that has been displaced by the changing boundaries of its partition. Remember to use the correct device designation. In this example, I use sda2 to represent Partition 2 on an internal SD card slot, but your may differ.
            $ sudo e2fsck -f /dev/sda2
            If e2fsck asks to create a Lost+Found directory, it's OK to allow it.
            The resize:
            $ sudo resize2fs /dev/sda2 
        
        Boot:
            Your system now occupies all available  space on your SD card. Put the card in your Nokia n900 and boot.Choose the u-boot shell. enter $ run sdboot shell.
            Once booted, verify your hard work with df:

    Configuring U-boot (optional)
        In order to configure pmos to boot by default on the N900, using U-boot, you will need to boot into Maemo and create a /etc/bootmenu.d/10-pmos.item file as the root user with these contents:
            $ vim /etc/bootmenu.d/10-pmos.item 
                ITEM_NAME="postmarketOS"
                ITEM_SCRIPT="boot.scr"
                ITEM_DEVICE="${EXT_CARD}p1"
                ITEM_FSTYPE="ext2"
            It can be set to the default boot option by creating a symlink:
            $ ln -s /etc/bootmenu.d/10-pmos.item /etc/default/bootmenu.item 
            Finally, run u-boot-update-bootmenu 
            Nokia-N900:~# u-boot-update-bootmenu
                Adding bootmenu entry for: 'Maemo 5 with attached kernel 2.6.28-omap1 (Internal Nand)'
                Configuration file: /etc/bootmenu.d/10-pmos.item
                Adding bootmenu entry for: 'postmarketOS'
                Configuration file: /etc/bootmenu.d/30-Kali_Linux-kali-rolling-armhf-4.5.0-rc1+.item
                Adding bootmenu entry for: 'Kali Linux kali-rolling armhf 4.5.0-rc1+'
                Generating u-boot bootmenu script...
        Note: This will set pmos as the default boot option. Maemo will still be accessible when booting the N900 with the keyboard slide out and selecting the relevant boot option in the u-boot menu.

    Configure 
        $ ssh chyiyaqing@172.16.42.1                                
        The authenticity of host '172.16.42.1 (172.16.42.1)' can't be established.
        ECDSA key fingerprint is SHA256:azUOL7+SVV8T+xDB9vRX/YmXNv3a8gE75SkVFmbTolA.
        Are you sure you want to continue connecting (yes/no)? yes
        Warning: Permanently added '172.16.42.1' (ECDSA) to the list of known hosts.
        chyiyaqing@172.16.42.1's password: 
        Welcome to postmarketOS!
        This distribution is based on Alpine Linux.
        Read both our wikis to find a large amount of how-to guides and
        general information about administrating and development.
        See <https://wiki.postmarketos.org> and <https://wiki.alpinelinux.org>.
        You may change this message by editing /etc/motd.
        nokia-n900:~$ 

```

i3wm
----
> I3wm is the recommended UI. It is lightweight and fast, and we have a custom N900 configuration that optimizes for its keyboard.The most important keybindings are describled below, for details see i3wm.conf. This file gets installed to ~/.i3/config and of course you can customize it. 
```
default mode:
    shift + space: switch to "command mode"

command mode:
    t: open terminal 
    k: kill current program 
    w: workspace mode 
    r: restart i3wm (use fater modifying the config)
    q: go back to "default mode"

workspace mode:
    a/s/d/f/g: switch to workspace 1/2/3/4/5
    q: go back to "command mode"

```

Kali Linux Rolling Edition 
--------------------------
* Installation instructions
    - Step 1: Get a 8GB or more sized memory card.
    - Step 2: Extract 'kali-rolling.7z' file, it will give you 'kali-roling.img' file.
    - Step 3: Write the extracted 'kali-rolling.img' file to your sdcard ($ sudo dd if=/path to th extracted .img file kali-rolling.img of=/dev/sdx bs=1M)
    - Step 4: Install U-Boot in your phone ($ apt-get install u-boot-flasher)
    - Step 5: Copy 'configure_u-boot.sh' file to your phone memory, and run it as root user ($ sudo gainroot then $ ./configure_u-boot.sh)
    - Step 6: Insert SDCARD into your phone and Switch off and slide up your phone then switch on. And choose Kali-Rolling OS from the list.
    - Step 7: Configure your Kali OS on your first boot.
    - Step 8: Login with username 'user' and password with the password that you have specified during configuration.
    - Step 9: After everything works fine, shutdown your device and resize your sdcard's existing partition using any parition using any partition managing tool and your can add a 'swap' partition to your sdcard if your want.
