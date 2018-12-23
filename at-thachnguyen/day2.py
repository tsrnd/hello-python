members = { 'Duc': 17, 'Huy': 14, 'Huyen': 20, 'Nhan': 30, 'Tuan': 23 }
names = members.keys()
for i in names:
  print(i)

print(type(names))
#-----------------
list_example = list(range(1,10))
for i in list_example[2:5]:
  print(i)
#-----------------
import time;
now = time.time()
print(now)
print(time.localtime())

import datetime
today = datetime.date.today()
print(today.strftime('Today is %d, %b %Y'))
print('Today is ' + today.strftime('%A'))
