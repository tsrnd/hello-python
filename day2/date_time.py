import time
import calendar

localtime = time.localtime(time.time())
print("Current time: ", localtime)
localtime = time.asctime(time.localtime(time.time()))
print("Curren time: ", localtime)

cal = calendar.month(2018, 2)
print(cal)
calendar.prcal(2017)
