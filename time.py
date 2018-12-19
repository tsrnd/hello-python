import time, calendar;      # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

# TimeTuple
print (time.localtime());

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

cal = calendar.month(2018, 12)
print ("Here is the calendar:")
print (cal)