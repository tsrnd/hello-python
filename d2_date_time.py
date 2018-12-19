import time
import calendar

ticks = time.time()
print("ticks:", ticks)

local_time = time.localtime()
print(local_time)

local_time = time.localtime(time.time())
print(local_time)

# format time
local_time = time.asctime(local_time)
print("Local current time:", local_time)

# calendar
cal = calendar.month(2018, 12)
print(cal)

# time module
local_time = time.localtime(time.time())
print(time.altzone)

print(time.asctime(local_time))

print(time.clock())

# calendar module
print(calendar.calendar(2018, w=2, l=1, c=6))
print(calendar.isleap(2000))
print(calendar.leapdays(2000, 2015))
print(calendar.month(2018, 12))
print(calendar.monthcalendar(2018, 12))
