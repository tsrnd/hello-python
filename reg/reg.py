import re

#Check if the string starts with "The" and ends with "Spain":
str = "The rain in Spain falls mainly in the plain!"
#first and last character 
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")


#findall
y = re.findall("aix*", str)
print(y)
if (y):
  print("Yes, there is at least one match!")
else:
  print("No match")

x = re.findall("plain", str)
if (x):
  print("Yes, the string ends with 'world'")
else:
  print("No match")