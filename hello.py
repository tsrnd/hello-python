# Number
import math
x = 5.2
y= math.ceil(x)
print("ceil(",x,") = ", y)
z = abs(-5)
print("abs(",-5,")= ",z)
t = math.floor(x)
print("floor(",x,") = ", t)
print("round of 5.2 = ", round(5.26,1))
print("\n\n\n#####End---Number#####\n\n\n")
#String
s1 = "Xin chao"
s2 = "Hello anna"
print("Length of '",s1, "' is: ", len(s1))
print("Number of character a in 'Hello anna' is :", s2.count('a') )
print(s1, " ends with 'chao' is : ", s1.endswith("chao"))
s3 = ("mot", "hai", "ba")
print(",".join(s3))
print("Replace: ", s1.replace("in","IN"))
print("Index: ", s1.index("chao"))
print("\n\n#####End-String######\n\n")

### List
list1 = ["Thai", "Le","Quang"]
print(list1[1])
del list1[1]
print("After delete list1[1]: ", list1)
list1.append("14T2")
print("After append list1: ", list1)
print("Index of Quang in list1: ", list1.index("Quang"))
print("\n\n#####End-List#####\n\n")

### Tuple
tuple1 = ("mon","tue","wed","thurs")
tuple2 = ("fri","sar","sun")
print("Tuple1: ",tuple1)
print("Concat tuple: ",tuple1 + tuple2)
print("Max of tuple1: ", max(tuple1))
print("\n\n#####End-Tuple#####\n\n")

### Dictinary
person = {"name": "thai", "age": 22, "school" : "DUT"}
print("Dictionc Person: ", person)
del person['age']
print("After remove a element key 'age': ", person)
print("Get key shool: ", person.get('school'))
print("Value of person: ", person.values())
print("\n\n######End-Dictionary#####\n\n")


### Date-time
import time

currentTime = time.localtime(time.time())
print("Current time: ", currentTime)

import calendar

print("2018 is leap year: ", calendar.isleap(2018))
cal = calendar.calendar(2018,12)
print("Calendar of 12th, 2018: ", cal)

