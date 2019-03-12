==== v0.X.N ($Id: README_FIRST.txt 11604 2015-02-23 02:18:36Z NiLuJe $) ====

This hack, based on ebs' code, restores `usbNetwork functionality.
If you don't know what that means, then you probably shouldn't even be trying to use this.

If you don't understand half of what's written here, see the previous paragraph.

As always, it may void your warranty, eat your Kindle, kill a kitten, and sell your first
born's soul to the devil.

I *strongly* recommend having a proper Linux CLI sysadmin background before trying to use this,
or you *WILL* probably end up messing your Kindle up. Do *NOT* do anything with this unless
your are *REALLY* sure you understand what you're doing.


=== Install/Uninstall/Upgrade ===

Nothing fancy, as usual, with a jailbroken Kindle, just use the appropriate update file:
copy it to the Kindle's USB drive's root, then launch it by going to [Menu] -> Settings -> [Menu] -> Update Your Kindle.
DO NOT reboot your device with a custom .bin in the Kindle's USB drive's root, it won't work.

When upgrading from a previous version, no need to uninstall anything first, the installer will take care of everything.
If you customized your config file, make sure you check the latest default config file to see if anything new was implemented.


=== Usage ===

I'm gonna assume Linux/BSD/OS X here, Windows people, you're on your own.
(Hint: Documentation/usb/linux.inf in the Linux source tree. The K4 Wiki page might aso be of some help).

* First of all, you'll need proper support for this stuff in your Kernel. (If you're using
OS X or aren't rolling your own kernel, you probably don't need to bother with this).

usbnet (CONFIG_USB_USBNET) & cdc_ether (CONFIG_USB_NET_CDCETHER)

(Still, a note to the poor Windows users: Yes, that means you'll need a non-default driver.)

* Plug & mount your Kindle.

* Take a moment to read, and edit, if need be, the config file in usbnet/etc/config.
In case you managed to miss the shiny warnings there: this *HAS* to use UNIX line endings,
and I really wouldn't recommend editing this while you're in usbnet mode.
(Note to K4 users: Make sure to keep USE_VOLUMD set to true, it's known to make things much smoother on the K4).

I'd also recommend making sure everything works with a plain eth over usb telnet/ssh shell
before fiddling around in there. Same thing with enabling the 'auto' enable at boot feature,
make sure everything works like you want it to before shooting yourself in the foot with that.

All of these settings are now available in a friendly KUAL menu :).
Running at least KUAL 2.1 is recommended for the best user experience.

* Now would be a good time to setup your public key if you intend to auth over SSH via shared keys.
Which you should, because it's awesome, especially with the help of an SSH agent :D.
The pubkeys are stored, in OpenSSH format, in usbnet/etc/authorized_keys (ie. you can safely use
a ~/.ssh/authorized_keys2 file from OpenSSH).
Also, it's the preferred method of auth when using SSH over WiFi, because it's way more elegant
than switching (or remembering) the root password (Because you *WILL* need to auth properly over WiFi).
For a quick HOWTO, check this post by ixtab: http://www.mobileread.com/forums/showpost.php?p=2598227&postcount=4

* unmount & eject your Kindle
(You might also want to unplug it, some devices behave strangely when toggling usbnet/usbms while plugged in).

* You'll need to be in debug mode to run private commands, so, on the Home screen, bring up the
search bar (by hitting [DEL] on devices with a keyboard, or the keyboard key on a K4, for example), and enter:

;debugOn

* And now we can enable usbnet:

~usbNetwork

(Or `usbNetwork on FW 2.x)

* Your Kindle should now be detected as something like a RNDIS/Ethernet Gadget or CDC Ethernet Device network adapter.

* If you don't need to enter any more private commands, switch debug off.

;debugOff

* Now, to actually connect to the device, we'll need to bring the shiny usb network interface
the kernel prepared for us. I'm assuming it's the only USB network interface in the system, so, usb0 on Linux.
I'm also assuming the default usbnet config, ie. HOST_IP=192.168.2.1 & KINDLE_IP=192.168.2.2

/!\ K4 users /!\
  On the K4, the defaults are different (to match Amazon's defaults in diags): HOST_IP=192.168.15.201 & KINDLE_IP=192.168.15.244

Note to OS X users: You'll have to configure the network interface manually via OS X's GUI (cf. http://www.mobileread.com/forums/showpost.php?p=2895606&postcount=13).

If you're also using a Kindle Touch or a Kindle 4 in diags, make sure you update your settings accordingly if you use some
kind of automated network setup (Windows/OS X/Network Manager), because those devices default to different settings.

Also, if your distribution is using a recent udev version, it might be using the new predictable network interface names
(cf. http://www.freedesktop.org/wiki/Software/systemd/PredictableNetworkInterfaceNames), so be wary of that.
You can get a hint of the correct name by piping the dmesg output to grep usb0: for example, on my box,
the current USB slot causes it to be named a very poetic enp0s26f7u5 (systemd-udevd[26718]: renamed network interface usb0 to enp0s26f7u5).

# ifconfig usb0 192.168.2.1

In a similar vein, if you plan to use more than one Kindle concurrently, you'll have to tweak the MAC addresses of the
USB network interface. For more detaisl about this kind of setup, you might want to check these two posts out:
http://www.mobileread.com/forums/showpost.php?p=1838544&postcount=2122 & http://www.mobileread.com/forums/showpost.php?p=1841893&postcount=29

* Depending on how your system set USB permissions up, you may still need to be root to connect to the device over USB.
I'm assuming you have a proper udev setup, so, I'll switch to a user shell now.

$ ssh root@192.168.2.2

or

$ telnet 192.168.2.2

Note that, when WiFi mode is enabled, telnetd won't be started, and the SSH daemon *WILL* require a proper password!
When WiFi mode is disabled, telnet will log you right in without password, and SSH will log you in with anything as
the password (even a blank one, so you can just type return).

* Like I said at the beginning, if you don't understand half of what you're doing here, go away before you brick your Kindle.
It's for your own good.

* When you're done, exit your shell on the Kindle, and bring the network interface down before ejecting/unplugging your Kindle.

# ifconfig usb0 down


=== Enable @ boot ===

If you want your Kindle to default to usbnet mode, instead of mass storage, drop a blank 'auto' file in the usbnet folder,
and restart your Kindle.

Make sure your setup/config is working before, though ;).

It should be starting a little while *before* the framework, so it's very, very useful to get out of a framework boot failure,
so if you're serious about playing with your Kindle, you'll probably want to run at least your main dev Kindle that way :).

If you're unsure about the timing, drop a blank 'verbose' file in the usbnet folder, that'll make the hack print important parts of
the log (like when the SSHD server is actually started) on the bottom of the screen.


=== Using OpenSSH instead of dropbear ===

You can now use OpenSSH instead of dropbear! Just set USE_OPENSSH to true in the config file, and restart your Kindle.

(If you customized your config file, you may have to update it with the latest default one found in the zip archive).

Keep in mind that OpenSSH will *ALWAYS* check the passwords, unlike dropbear in non-wifi mode, so, make sure you auth via shared keys, or know
your passwords! (Hint: run kindletool info $(cat /proc/usid) on your device ;). Unless you already changed your password once, the first password shown will be the right one).

Why would you want to use OpenSSH? Simply because the login is quite a bit faster if your client doesn't handle ECC key exchanges…
(There's apparently a regression in dropbear/libtom{crypt,math} that slows it down to noticeable levels, and the libtomfastmath branch of dropbear is even worse on the Kindle…).


=== Notable changes ===

Works on FW 2.x, 3.x & 4.x

Note that since FW 3.x, the private command prefix has been changed to ~ instead of `
(But private commands are still only available in debug mode).

SFTP & SCP support.

SSH/SFTP over WiFi support (check usbnet/etc/config). Note that when WiFi mode is enabled, passwords
*WILL* be checked. So make sure you know it, or auth via shared keys.

IP addresses configuration is done in usbnet/etc/config instead of in the usbnetwork script.

Shared key auth support. Store your public keys in usbnet/etc/authorized_keys (OpenSSH format).
You can safely use an OpenSSH ~/.ssh/authorized_keys2 file for example.

The usbnetwork script is now a toggle, meaning that if you enter the ~usbNetwork command
a second time, it'll switch back to USB Mass Storage mode, and stop telnetd & sshd, without having
to reboot your Kindle.
Don't forget to drop back to ;debugOff before using your Kindle normally, though.

Optionally use OpenSSH instead of dropbear.

Bundles a number of useful tools (OpenSSH, rsync, mosh, sshfs, kindletool, htop, lsof, fbgrab, strace, elfutils, nano, zsh).

The busybox build includes the full ash shell, and we also bundle zsh. Since they live in the userstore,
do NOT change the default shell of an account to those. You can instead try to launch them automatically
by abusing the command option in your authorized_keys file, or use local aliases.
Don't forget to run login shells (usually by passing the -l to your shell).

The tethering scripts (Use Host networking on the Kindle) are in usbnet/bin/usbnet-*
They're pretty much untested, and I'm not precisely enclined to really support them,
so, you're on your own, and use at your own risk.

=== BUGS ===

In order to avoid the "nothing is exported over usb ms" issue after an update,
your Kindle will automatically switch back to USB MS before launching the update process.

To that effect, I'd recommend properly exiting your shell sessions and unplugging your Kindle
before launching an update, or wall will shout at you, and your terminal will freeze ;).

In the same vein, avoid booting your Kindle while plugged to a computer, it tends to make weird things happen on most devices…
And don't think that USE_VOLUMD will help, it won't. For example, on a K4, it fails spectacularly with a:
modprobe: FATAL: Error inserting g_ether (/lib/modules/2.6.31-rt11-lab126/kernel/drivers/usb/gadget/g_ether.ko): Device or resource busy

If you encounter any of these issues, of if your Kindle shows the "USB Drive Mode" screen when it is in fact in usbnet mode,
try setting USE_VOLUMD to true in the config file (while in usbms mode), and restart your Kindle.
There *might* still be some timing issues left when using volumd (noticeable if your kindle blocked for 15s when toggling usbNetwork):
if you can't seem to get into your Kindle, try using the default IP: ifconfig usb0 192.168.15.201 && ssh root@192.168.15.244

On FW 2.x & 3.x, you might want to kill netwatchd to prevent it from killing connections left & right…
(It'll happily break *outgoing* ssh connections, like sshfs, for example).

For the adventurers using FW 3.x on a DXG, for some unkown reason, the usbNetwork private command is broken.
Use the KUAL extension, or launchpad (http://www.mobileread.com/forums/showthread.php?t=97636),
with the following action file (let's say, in launchpad/usbnet.ini):

[Actions]
# Toggle USB Network
Shift N = !/test/bin/usbnetwork

--NiLuJe
