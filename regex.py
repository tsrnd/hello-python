import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")


#Replace all white-space characters with the digit "9":

str = "The rain in 12 Spain"
x = re.sub("\d", "#", str)
print(x)