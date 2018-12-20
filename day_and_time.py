import time
import calendar

print()
localtime = time.localtime(time.time())
print ("Local current time :", time.localtime())
print("clock",time.clock())
print("ctime",time.ctime())
print ("Start : %s" % time.ctime())
time.sleep( 0.5 )
print ("End : %s" % time.ctime())
print()

cal = calendar.month(2019, 2)
print ("Here is the calendar:")
print (cal)
print("nam nhuan : ".capitalize(),calendar.isleap(2028))
print(calendar.firstweekday())
