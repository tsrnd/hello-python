import re

line = "Cats are smarter than dogs 573fdfd964"

searchObj = re.search(r'(.*) are (.*?) .* (\d+).*(\d+)$', line, re.M | re.I)

if searchObj:
    print("Serarch group(): ", searchObj.group())
    print("Serarch group(1): ", searchObj.group(1))
    print("Serarch group(2): ", searchObj.group(2))
    print("Serarch group(3): ", searchObj.group(3))
    print("Serarch group(4): ", searchObj.group(4))
else:
    print("Nothing mathch")

line2 = "foo1\nfoo2\n"

searchObj2 = re.search(r'foo.$', line2, re.M)
print("seach in line2: ", searchObj2.group())

line3 = "foo\n"
print("search in line3: ", re.search(r'$', line3, re.M).groups())
