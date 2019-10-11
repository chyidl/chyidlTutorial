macOS 
=====
> Mac OS,Mac OS X, or macOS, is the operationg system that resides on Apple's desktop and portable computer lineup. Built upon a Unix core, it is easy to use yet highly advanced, extremely stable, and an excellent OS for productivity and creation. Browse through our articles or use the search feature to look for something specific that is pertinent to the Mac operating system.will bring the latest in cool macOS tips, and everything else related to Apple's awesome macOS operating system!

macOS Intro 
-----------
> macOS is a series of graphical operating systems developed and marketed by Apple Inc.

![Unix-like operating systems](/imgs/os/macOS/900px-Unix_timeline.en.svg.png?raw=true)

At macOS's core is a POSIX compliant operating system built on top of the XNU kernel, with standard Unix facilities available from the command line interface. Apple has released this family of software as a free and open source operating system named Darwin. On top of Darwin, Apple layered a number of components, including the Aqua interface and Finder, to complete the GUI-based operating system which is macOS.


macOS Tips
----------

**Tutor macOS via Command Line**
> The macOS command line interface is home to thousands of programs that the average user doesn't know exists. Leveraging years of hard work by the GNU foundation and others in the open source community,Apple designed a wonderful OS that doesn't need any use of the command line. While using the command line in macOS is not necessary for the every day operation of macOS, if harnessed correctly, it can save you a lot of time, and occasionally give you a laugh. I hope you enjoy these macOS
command line utilities!

![Unix command line](/imgs/os/macOS/retro-terminal-mac-screenshots-2.jpg?raw=true)

```
# **1. ssh**
# my personal favorite is using ssh as a SOCKS server to browse the web securely in public internet locations.

# **2. top**
# how a list of every process currently running on your macOS.

# **3. say**
# this command is unique to macOS, and offers more fun than anything else.

# **4. softwareupdate**
# The "softwareupdate" command is a quick and easy way to install software updates from apple.
$ softwareupdate -i -a  # to install all available updates for your macOS.
$ softwareupdate -i -r  # to install "recommended" updates type

# **5. ifconfig**
$ ifconfig | grep inet  # return just the ip information for my macOS 
$ ifconfig en0 up | down # on|disable a network interface, This can be much quicker than using the System Preferences window
# Get your internal IP, you can do the following 
$ ipconfig getifaddr eth0 
# Get external IP address 
$ curl ipecho.net/plain ; echo

# **6. screencapture**
# screencapture offers a more advanced way to take screen captures 
$ screencapture -iW ~/Desktop/screen.jpg  # 
$ screencapture -S ~/Desktop/screen.jpg # take a snapshot of your entire screen by typing 

# **7. whois**
# WHOIS searches 
$ whois chyidl.com 

# **8. open**
$ open https://apple.com  # open the URL in the system's default browser.

# **9. pbcopy|pbpaste**
# copy the output of a shell command 

# Command Line Keyboard Shortcuts for macOS 
#
# Ctrl + A      : Go to the beginning of the line your are currently typing on
# Ctrl + E      : Go to the end of the line you are currently typing on 
# Ctrl + L      : Clears the Screen, similar to the clear command 
# Ctrl + U      : Clears the line before the cursor position. If you are at the end of the line, clears the entire line. 
# Ctrl + H      : Same as backspace 
# Ctrl + R      : Let's you search through previously used commands 
# Ctrl + C      : Kill whatever you are running 
# Ctrl + D      : Exit the current shell 
# Ctrl + Z      : Puts whatever you are running into a suspended background process. fg restores it. 
# Ctrl + W      : Delete the word before the cursor 
# Ctrl + K      : Clear the line after the cursor 
# Ctrl + T      : Swap the last two chracter before the cursor
# Esc  + T      : Swap the last two words before the cursor

# sysctl 
$ sysctl -n machdep.cpu.brand_string 
# format: Chip Brand - Processor Type and Chip Model - CPU Speed 
Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz
$ system_profiler | grep Processor
```

**Anytime I find myself doing a repetivive task, it is crucial that I discover small tricks and workarounds to make my daily routine as efficient as possible.**

1. Diagnose and Fix System Problems
    If you're having any problems with your macOS, go over this great list and try out the troubleshooting methods described, you just may fix the problem yourself!

```
**FIRST AID**
a. 01 Restart 
b. 02 Check/fix the filesystem 
c. 03 Make sure you're not running out of free space on the System volume 
d. 04 Repair permissions 
e. 05 Create a new user account, and see if the problem persists there 
f. 06 Clear system & user caches 
g. 07 Disable Application Enhancer, if you're running it 
h. 08 Startup in SafeBoot mode, and see if the problem persists there 
i. 09 Reset system firmware 
j. 10 Upplug all USB,Firewire devices except Apple mouse 
k. 11 Reapply the latest combo updater 
l. 12 Run the Apple hardware diagnostic CD 
m. 13 Check the hard drive for bad blocks 
n. 14 Take out 3rd Party PCI cards 
o. 15 Upplug 3rd Party PCI cards
p. 16 Reset PMU 
q. 17 Archive and reinstall the OS 
r. 18 Reinstall the system from scratch 
s. 19 Send the machine back to Apple 
t. 20 Additional Notes 
```

2. An advanced script/web solution to track stolen Macs
    macOS doesn't provide Access Mac Camera by Command Line. a third party utility named ImageSnap is the best route to taking captures from command line. 

```
1. What this essentially will do:
    a. The Mac will report in to a server (to see if it is stolen) every six minutes 
    b. It will run in the background without the user ever knowing. It is a LaunchDaemon -- which means it will work even if no user is logged into the background
    c. If it is stolen, it will send information from the machine back to you through FTP 
    d. If wanted, it will take a picture using the built-in iSight camera 
    e. If wanted, it will move the Finder.app and Dock.app to a different location, which is easy to put back into place, and then change the background picture to an error message saying the Finder is corrupt and to return the computer to an Apple store for a free fix. 

2. Little bits of info about the script 
    The script is called up by a launch daemon every six minutes. If the Mac is on the internet, it will attempt to contact your webserver. If you server is up, it will look for a webpage that is named by your computer's MAC address.html, If this page 

**Install ImageSnap**
$ brew install imagesnap 

# Take a Photo 
# To Take a photo using the default video input device (FaceTime HD Camera is the default in most newer Macs)
# take image, let camera warm up 1 second 
$ imagesnap -w 1 snapshot.png 
# You'll wait a brief second or two, your green camera indicator will light up, and will then quickly fade out. The image will be saved to a **snapshot.png** file

# imagesnap -t {x}:{yy} seconds 
# The command above takes a photo every second until the process is killed.
imagesnap -t 1 -w 1 

``` 

3. Automate YouTube Video and MP3 Rips with Bash Shell
    Take YouTube videos linked in a text file and download them and Convert to MP3 format 

```
# The Text File
http://www.youtube.com/watch?v=iYtDqHupwrg
http://www.youtube.com/watch?v=xZ23pVTPfSw
http://www.youtube.com/watch?v=Rvw1ctGWfSs
http://www.youtube.com/watch?v=IXPOHCsgWFw

# The Bash Script -- ??
#!/bin/sh 
IFS=$'\n'
for line in `< songs.txt`; do 
	newfile=`youtube-dl -o %\(title\)s.%\(ext\)s $line | grep '^\[download\]' | cut -d ' ' -f 3-`
	ffmpeg -b 192k -i $newfile ${newfile/flv/mp3}
	rm $newfile
done

# script reads the file by line, downloads the YouTube video at the links privided by the text document, uses ffmpeg to rip the song into an mp3, and deleted the video. Note that you'll need YouTube-DL and FFMPEG to run this script; 
```

4. Create an Image Preview from a Video 
![Image Preview](/imgs/os/macOS/imagePreview.png?raw=true)
```
# use two utilities, ffmpeg and ImageMagick to create preview image 
# Use ffmpeg to Take Screenshorts at Set Intervals 
# ffmpeg is the best utility to take screenshorts on intervals 

# Take a screencap every second 
$ ffmpeg -i imovie_mac_4k_film.mp4 -vf fps=1 video-caps/cap%d.png

# Take a screencap every minute 
$ ffmpeg -i imovie_mac_4k_film.mp4 -vf fps=1/60 video-caps/cap%03d.png

# Take a screencap every ten minutes
$ ffmpeg -i imovie_mac_4k_film.mp4 -vf fps=1/600 video-caps/cap%04d.png

# Depending on the length of video, you'll want to use one of the preceding shell command formats. You may want to do the match
# to check video length and create a given number of thumbnails

# Use ImageMagick to Merge Images 
# While ffmpeg is great for video manipulation, ImageMagick is its image counterpart. Join images into one is incredibly easy 

# Append images vertically "-append"
$ convert video-caps/*.png -append video-caps/all.png 

# Append images horizontally "-append"
$ convert video-caps/*.png +append video-caps/all.png 

# if you want to open the image in your default image viewers
# open with the default app 
$ open all.png 

# Open with a specific app 
$ open -a /Applications/Firefox.app all.png 
``` 

5. Get Image Dimensions from Command Line 
```
# Using ImageMagick you can find the dimensions of an image from command line 

# Get the size of a JPG 
$ convert photo.jpg -print "Size: %wx%h\n" /dev/null  
# Size: 3840 x 8640 

# You can get the image dimensions of any image type from PNG to JPG to GIF to even PSDs.
```

6. Extracting RAR Files in Terminal
```
$ brew install unrar

# Listing contents inside the RAR file 
$ unrar l file.rar

# Testing the RAR file 
$ unrar t file.rar

# Unrar-ing the file 
$ unrar x file.rar

# extract the contents of the file.rar to a particular directory
$ unrar e file.rar /pathToExtractTo
```

Spoofing a Mac Address in macOS Mojave 
--------------------------------------
```
spoof a MAC address on a macOS computer running Majave. This is a technique for changing the factory-assigned physical Media Access Control(MAC) address of a network interface on a networked device to a random address.

1) Determine the name of the Wi-Fi interface on your Mac 
    Depending on the Mac you're using, the Wi-Fi interface can have one of several names, usually en0 or en1. 
    hold down the Option key and click on the Wi-Fi icon on the menu bar 
        Interface Name: eh0 
2) Temporarily disable Wi-Fi
    When spoofing the MAC address on our Mac, Wi-Fi must be temporarily disabled. 
3) Launch Terminal 
4) Verify the existing MAC address 
    $ ifconfig en0 | grep ether 
5) Generate a random hexadecimal number to serve as the "new" MAC address 
    $ openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//'
6) Copy the random address from Terminal, then type the following command and paste the random address at the end before pressing Return 
    $ sudo ifconfig en0 ether bd:5d:26:d9:4a:b2 
```

Add a Message to the Login and Lock Screen in Mac OS X 
------------------------------------------------------
```
OS X has a nice new feature to login and lock screens that allow you to display a meesage underneath the login panel. This is visible to everyone who can see the Mac screen, and it makes for a great place to put either a bit of generic personalization message, or better yet, a lost & found message with some contact and ownership details 

1. Open up System Preferences from the  Apple menu > System Preferences > Security & Privacy > General > then click the little lock icon in the lower left corner of the window, enter the admin password when asked. 
2. Check the button next to "Show a message when the screen is locked"
3. Click the lock icon again to set the changes and close out System Preferences.
```

You can see what this looks like in the screenshot above and the closeup image below.
![Lock Message](/imgs/os/macOS/Screen_Shot_LockMessage.png?raw=true)

Having a message on your lock screen is a great loss prevention and general anti-theft measure, since anyone who gets the Mac into their hands later will see the message and if they have a conscience, will hopefully call the number your set on the screen. This could also help if you ever acciendtally misplaced a Mac laptop


Install Multiple Java Versions on macOS 
---------------------------------------

> On Mac, Homebrew is the de-facto package manager, and Homebrew Cask is the app manager

```
Install Homebrew Cask first if you havn't:
$ brew update
$ brew tap caskroom/cask 
$ brew install brew-cask-completion 

If you brew or cask is outdated, update and upgrade:
$ brew update && brew upgrade brew-cask-completion && brew cleanup && brew cask cleanu
# Check if we already have JDK 7, 11 installed by Homebrew Cask:
$ brew tap caskroom/versions 
$ brew cask info java7 
$ brew cask info java11 

To check JDK 12 (latest)
$ brew cask info java 

Install Java 7, 11 (latest):
$ brew tap caskroom/versions
$ brew cask install java8
$ brew cask install java11 

Install OpenJDK Versions 7, 11 
$ brew tap AdoptOpenjdk/openjdk
$ brew search /adoptopenjdk/ 
```
