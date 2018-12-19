import time
import calendar

print(time.localtime(time.time()))
print(time.time())
print(time.timezone)

cal = calendar.calendar(2018)
August = calendar.month(2018, 8)
weekday = calendar.weekday(2018, 8, 9)

print(cal)
print(August)
print(weekday)
