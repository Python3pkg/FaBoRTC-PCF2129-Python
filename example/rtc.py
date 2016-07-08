# coding: utf-8
## @package FaBoRTC_PCF2129
#  This is a library for the FaBo RTC I2C Brick.
#
#  http://fabo.io/215.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBoRTC_PCF2129
import time
import sys

rtc = FaBoRTC_PCF2129.PCF2129()

# 日付時刻の設定
print "set date/time"
rtc.setDate(
    2016, # Years
    7,    # months
    8,    # days
    12,   # hours
    1,    # minutes
    50)   # seconds

while True:
    # 日付時刻の取得
    now = rtc.now()

    # 日付時刻の表示
    sys.stdout.write(str(now['year'])  + '/')
    sys.stdout.write(str(now['month']).zfill(2) + '/')
    sys.stdout.write(str(now['day']).zfill(2)   + ' ')

    sys.stdout.write(str(now['hour']).zfill(2)    + ':')
    sys.stdout.write(str(now['minute']).zfill(2)  + ':')
    sys.stdout.write(str(now['second']).zfill(2))
    print
    time.sleep(1)
