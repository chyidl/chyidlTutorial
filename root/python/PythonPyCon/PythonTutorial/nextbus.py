#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# nextbus.py
import urllib.request
import sys

print("Command options:", sys.argv)

if len(sys.argv) != 3:
    raise SystemExit('Usage: nextbus.py route stopid')

route = sys.argv[1]
stopid = sys.argv[2]
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route, stopid))
data = u.read()

from xml.etree.ElementTree import XML

doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.text)
