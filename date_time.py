print('= Date Time =')

import time
import calendar

now = time.localtime()
print('now (local) =', time.asctime(now), time.tzname[1])
now = time.gmtime()
print('now (utc) =', time.asctime(now))
'''
now (local) = Mon Dec 24 14:34:56 2018 +07
now (utc) = Mon Dec 24 07:34:56 2018
'''

cal = calendar.month(2018, 12)
print('calendar =\n', cal)
'''
calendar =
    December 2018
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31
'''
