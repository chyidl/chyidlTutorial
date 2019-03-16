#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# time_get_lock_info.py
# utils
#
# 🎂"Here's to the crazy ones. The misfits. The rebels.
# The troublemakers. The round pegs in the square holes.
# The ones who see things differently. They're not found
# of rules. And they have no respect for the status quo.
# You can quote them, disagree with them, glority or vilify
# them. About the only thing you can't do is ignore them.
# Because they change things. They push the human race forward.
# And while some may see them as the creazy ones, we see genius.
# Because the poeple who are crazy enough to think thay can change
# the world, are the ones who do."
#
# Created by Chyi Yaqing on 03/16/19 12:01.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the MIT

"""
时钟的实现与C库函数绑定在一起，所以一些细节使基于特定平台的
"""
import os
import textwrap  # Text wrapping and filling
import time  # Time access and conversions
import hashlib


available_clocks = [
    ('clock', time.clock),
    ('monotonic', time.monotonic),
    ('perf_counter', time.perf_counter),
    ('process_time', time.process_time),
    ('thread_time', time.thread_time),
    ('time', time.time),  # epoch [Unix time 1970.1.1 00:00] 开始之后的秒数以浮点数格式返回
]


for (clock_name, func) in available_clocks:
    print(textwrap.dedent('''\
            {name}:
            adjustable      : {info.adjustable}
            implementation  : {info.implementation}
            monotonic       : {info.monotonic}
            resolution      : {info.resolution}
            current         : {current}
        ''').format(
            name=clock_name,
            info=time.get_clock_info(clock_name),
            current=func()))


# time.time() 从[epoch] 开始以后以浮点数格式返回秒
print("The time is: ", time.time())

# time.ctime() Convert a time expressed in seconds since the epoch to a string
# representing local time
print('The time is      :', time.ctime())
later = time.time()+15
print('15 secs from now :', time.ctime(later))

# time.time() 函数返回的是系统时钟可以被用户或者系统服务更改，所以重复调用time()函数产生的
# 时间值可能会前后波动。monotonic()函数总是返回前向的时间值
# The monotonic is not affected by system clock updates.
start = time.monotonic()
time.sleep(0.1)
end = time.monotonic()
print('start    : {:>9.2f}'.format(start))
print('end      : {:>9.2f}'.format(end))
print('span     : {:>9.2f}'.format(end - start))

# time.perf_counter() : fractional seconds of a performance counter
# 用于计算 sha1校验和的数据
data = open(__file__, 'rb').read()

loop_start = time.perf_counter()

for i in range(5):
    iter_start = time.perf_counter()
    h = hashlib.sha1()
    for i in range(300000):
        h.update(data)
    cksum = h.digest()
    now = time.perf_counter()
    loop_elapsed = now - loop_start
    iter_elapsed = now - iter_start
    print(time.ctime(), ': {:0.3f} {:0.3f}'.format(iter_elapsed, loop_elapsed))

# struct_time : The type of the time value sequence returned by


def show_struct(s):
    print('     tm_year :', s.tm_year)
    print('     tm_mon  :', s.tm_mon)
    print('     tm_mday :', s.tm_mday)
    print('     tm_hour :', s.tm_hour)
    print('     tm_min  :', s.tm_min)
    print('     tm_sec  :', s.tm_sec)
    print('     tm_wday :', s.tm_wday)
    print('     tm_yday :', s.tm_yday)
    print('     tm_isdst:', s.tm_isdst)


print('gmtime: UTC')
show_struct(time.gmtime())
print('\nlocaltime:')
show_struct(time.localtime())
print('\nmktime:', time.mktime(time.localtime()))

# 当前时间依赖于时区设置, 时区可以由程序设置，也可以使用系统默认时区设置
# 改变时区并不会改变实际的时间，只是改变它的表现方式


def show_zone_info():
    print(' TZ      :', os.environ.get('TZ', '(not set)'))
    print(' tzname  :', time.tzname)
    print(' Zone    : {} ({})'.format(time.timezone, (time.timezone / 3600)))
    print(' DST     :', time.daylight)
    print(' Time    :', time.ctime())
    print()


print('Default :')
show_zone_info()

ZONES = [
    'GMT',
    'Asia/Hong_Kong',
]


for zone in ZONES:
    # 改变时区，首先设定环境变量TZ,然后调用tzset()
    os.environ['TZ'] = zone
    time.tzset()
    print(zone, ':')
    show_zone_info()

# 解析和格式化时间
# strptime() strftime()
now = time.ctime(1552717743.187825)
print('Now:', now)

parsed = time.strptime(now)
print('\nParsed:')
show_struct(parsed)

print('\nFormatted:', time.strftime("%a %b %d %H:%M:%S %Y", parsed))
