import re

line = "xin chao thai le"

matchObj = re.match(r'thai', line)

if matchObj:
    print(matchObj.group())
else:
    print('No match ')
searchObj = re.search(r'thai', line)

if searchObj:
    print(searchObj.group())
else:
    print('No search')
