import re

line1 = "LaHao"
line2 = "xinToi\nLaThai\nLaPha "

print("Non-Multipline: ")

search1 = re.search('^La', line1)
search2 = re.search('^La', line2)

if search1:
    print(search1.group())
else:
    print("No match s1")
if search2:
    print(search2.group())
else:
    print("No match s2")

print("Mulipline: ")

search1 = re.search('^La.*', line1, re.M)
search2 = re.search('(^La.*)', line2, re.M)

if search1:
    print(search1.group())
else:
    print("No match s1")
if search2:
    print(search2.group())
else:
    print("No match s2")

print("With $")
print("mulitple")

line1 = "LaHaoThaile"
line2 = "xinle\ntaole"

search1 = re.search('.*le$', line1, re.M)
search2 = re.search('(.*le$)', line2, re.M)

if search1:
    print(search1.group())
else:
    print("No match s1")
if search2:
    print(search2.groups())
else:
    print("No match s2")