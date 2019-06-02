eMac Specs

- 1.0 GHz PowerPC G4
- 17" CRT Display 
- 1GB SDRAM
- SuperDrive
- 60 IDE Drive 

Hold Key: Option + F + O 

For some reason the eMac won't boot the flash drive, either by running the installer and rebooting or holding option when booting...it doesn't show up in the open firmware boot loader.

* Boot a PowerPC Apple from USB 
> Booting from USB for PowerPC (PPC) eMac's is problematic to say the least. In any case, my 1ghz G4 Open Fireware version won't support it without getting acquanted with Open Firmware. After some serious digging around and rather a lot of experimenting I found a way though:
    - 1. Be sure to partition the disk with an Apple Partition Map (i.e. not GUID or MBR)
    - 2. Determine the partition where your bootable images it situated (e.g. an MacOS X DVD or DMG restarted to a partition with Disk utility's restore). This might be disk1s3 in which case the partition number is 3.
    - 3. Restart your iMac while holding down Command-Option-O-F (Alt-Cmd-O-F). This will load you in Open Firmware.
    - 4. Type:
```
dev / ls
to get the device tree/list 
Look for something in the output like:

/usb@b
    /disk@1 

As we're talking about a tree here, write down the complete path to this node. In my case it would be:
/ht/pci@2/usb@b/disk@1
```
    - 5. Type:
```
devalias ud /ht/pci@2/usb@b/disk@1
In other words: make 'ud' equal to the path you found in step 4.
```
    - 6. Now verify you got the right disk:
```
dir ud:3,\
(3 is the partition number you wrote down in step 2)
And look for a file with tbxi attribute, probably in:
\System\Library\CoreServices\BootX, e.g:
dir ud:3,\System\Library\CoreServices 
```
    - 7. The boot from it:
```
boot ud:3,\System\Library\CoreServices\BootX 
```
    - 8. Presto!
