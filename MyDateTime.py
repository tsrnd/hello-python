import time
import calendar

localtime = time.asctime(time.localtime(time.time()))
print("Local current time: ", localtime)
print(time.altzone)
print(time.time())
print(time.timezone)

cal = calendar.month(2018, 12)
print("This is clendar ")
print(cal)

print("This is list int clendar")
print(calendar.monthcalendar(2018, 12))

print("This is list int after set first week day ")
calendar.setfirstweekday(2)
print(calendar.monthcalendar(2018, 12))

a = calendar.monthrange(2018, 12)
print("First day on month =", a[0], " . Count day on month", a[1])

print ("My birth day is [0 (Monday) to 6 (Sunday)]",calendar.weekday(1997,4,10))
