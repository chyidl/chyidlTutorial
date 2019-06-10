Apple eMac G4/1.0 (ATI Graphics) Speces
=======================================

- 1.0 GHz PowerPC 7445 (G4)
- 17" Flat CRT Display; Resolution Support: 1024x768 
- 1GB SDRAM
- SuperDrive
- 60 IDE Drive 
- Genesis emulator()

* Boot a PowerPC Apple from USB 
> Booting from USB for PowerPC (PPC) eMac's is problematic to say the least. In any case, my 1ghz G4 Open Fireware version won't support it without getting acquanted with Open Firmware. After some serious digging around and rather a lot of experimenting I found a way though:
```
    - 1. Be sure to partition the U disk with an Apple Partition Map (i.e. not GUID or MBR; However PowerPC Macs can read GUID, just can't boot of GUID)
    - 2. Determine the partition where your bootable images it situated (e.g. an MacOS X DVD or DMG restarted to a partition with Disk utility's restore). Don't choose whole USB disk to restore. choose sub partition right. This might be disk1s3 in which case the partition number is 3.
    - 3. Restart your iMac while holding down Command-Option-O-F (Alt-Cmd-O-F). This will load you in Open Firmware.
    - 4. Apple Open Fireware Type:
dev / ls
to get the device tree/list 
Look for something in the output like:

/usb@b
    /disk@1 

As we're talking about a tree here, write down the complete path to this node. In my case it would be:
/ht/pci@2/usb@b/disk@1
    - 5. Type:
devalias ud /ht/pci@2/usb@b/disk@1
In other words: make 'ud' equal to the path you found in step 4.
    - 6. Now verify you got the right disk:
dir ud:3,\
(3 is the partition number you wrote down in step 2)
And look for a file with tbxi attribute, probably in:
\System\Library\CoreServices\BootX, e.g:
dir ud:3,\System\Library\CoreServices 
    - 7. The boot from it:
boot ud:3,\System\Library\CoreServices\BootX 
    - 8. Presto!
```

Reset Your Mac Password
-----------------------
* Reset Mac Password - without a CD or Boot Drive

> Using a pretty nifty trick you can reset a forgottern Mac password without a Mac OS X Installer CD/DVD or any kind of boot drive or recovery partition, and without having an Apple ID. This is basically the be-all-end-all approach if nothing else works, because it's guaranteed to get you back into a Mac when the other options are available, and it works in literally all version of OS X. 

```
The steps may seen a little intimidating at first but I assure you it's easy if you follow them
exactly, here is exactly how to do this in three stages:

Stage 1) Boot into Single User Mode and remove a setup file 
    * Restart the Mac holding down the Command+S keys, this will take you into Single User Mode and it's Terminal interface.
    * You'll need to check the filesystem first:
    $ fsck -fy
    
    * Next, you must mount the root drive as writeable so that changes will save:
    $ mount -uw / 
    
    * Now, type the following command exactly, followed by the enter key:
    $ rm /var/db/.applesetupdone 

    * After removing the applesetupdonw file, you need to reboot, type 'reboot' and hit enter 
```
