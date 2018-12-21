import time
import datetime
current = time.time()
print("Number of seconds elapsed since 12:00am, January 1, 1970:", current)
# output Number of seconds elapsed since 12:00am, January 1, 1970: 1545289992.88739

print(time.localtime())
# time.struct_time(tm_year=2018, tm_mon=12, tm_mday=20, tm_hour=14, tm_min=13, tm_sec=12, tm_wday=3, tm_yday=354, tm_isdst=0)

localtime = time.localtime(time.time())
print("Local current time :", localtime)
# output Local current time : time.struct_time(tm_year=2018, tm_mon=12, tm_mday=20, tm_hour=14, tm_min=13, tm_sec=12, tm_wday=3, tm_yday=354, tm_isdst=0)

print(time.asctime())
# output Thu Dec 20 14:13:12 2018

print(time.ctime())
# output Thu Dec 20 14:13:12 2018

print(time.sleep(4))
print(time.ctime())
# output Thu Dec 20 14:13:16 2018

### Getting the weekday of a certain date ###
todate = datetime.date(2018, 12, 20)  # year, month, day
print(todate.strftime("%A"))
# output Thursday

mybirthday = datetime.date(1996, 3, 2)
print(mybirthday.strftime("%A"))
# output Saturday
