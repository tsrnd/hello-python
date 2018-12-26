import re, pylint

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if (x):
    print("YES! We have a match!")
else:
    print("No match")

y = re.search("Portugal", txt)
print(y)

z = re.findall("ai", txt)
print(z)

t = re.search("\\s", txt)
print("The first white-space character is located in position:", t.start())

a = re.split("\\s", txt)
print(a)
