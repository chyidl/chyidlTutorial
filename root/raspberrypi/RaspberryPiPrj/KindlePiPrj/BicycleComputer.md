Build a Readable Bicycle Computer
=================================
> A Kindle and a Raspberry Pi make for a impressive display of maps and distance.

* requirement
```
    1. Raspberry Pi 
    2. Adafruit FONA 808 Cellular + GPS Breakout 
    3. Two reed switches mounted to the frame of my bike sense wheel rotation and pedal cadence by virtue of magnets attached to a spoke and to the inner chain ring. These switches are electrically connected to pins on the Raspberry Pi's GPIO (general purpose input/output) port, allowing the Pi to know how fast the wheels and pedals are turning.
    4. hostadp: which transform the Pi into a wireless access point.
    5. flask: a lightweight framework for writing Web application in Python 
    6. gpsd: parse the GPS data
    7. Leaflet: is the leading open-source JavaScript library for mobile-friendly interactive maps.

There were two notable complications
    1. One arose because of the way E-Ink works. It's very susceptible to ghosting, where pixels don't properly switch to a new state, so Amazon.com's engineering arranged for the Kindle's browser to cycle the entire display from black to white and back again when a new page loads. This initially made for awkward flickering, because my initial app sent a new page with updated values every second. The solution was to use what's known in Web-development circles as Ajax techniques to update just the necessary elements without sending a whole new page and triggering a refresh.

    2. Another twist peculiar to the Kindle is that when it connects to a new access point, it immediately tries to reach Amazon. If it doesn't get the right response, it won't treat the access point as valid.The solution was simple: Have the Pi supply the Kindle with the short response it was expecting from Amazon.

In the end, managed to pull together a system that shows distance, instantaneous speed, average speed, cadence, elapsed time, and clock time all at once. with digits large enough to read without squinting. Swiping and pressing buttons brings up other screens that offer such gooides as real-time mapping and logging.
```