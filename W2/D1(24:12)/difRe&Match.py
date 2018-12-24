import re

line = "Hoc Python la de nhat?";

matchObj = re.match( r'thon', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("Khong co ket noi!!")

searchObj = re.search( r'thon', line, re.M|re.I)
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
else:
   print ("Khong tim thay!!")