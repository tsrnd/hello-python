# Number
x = 1 
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))

# Cast
a = "1"
b = 2
c = a + str(b)
print(c)

# String
name = "quangchau"
print("Get letter by index:" + name[0])
print("SubString:" + name[2:5])
print("--------------------------------")

# List
foody = ["banana", "apple", "orange"]
foody.append("banana")
foody.insert(0,"hahah")
for x in "banana":
  print(x)
print("List--------------------------------")

# Tuple  same immutable kotlin
tupleList = ("banana", "apple", "orange")
for e in tupleList:
  print(e)
print("--------------------------------")

# Set
setList = {"banana", "apple", "orange"}
for element in setList:
  print(element)
print("--------------------------------")

# Dictionnary: element is key and value
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(thisdict.get("brand"))

# Iterable
print("Iterable--------------------------------")
foody = ("banana", "apple", "orange")
list = iter(foody)
for x in list:
 print(x)

import mymodule
# Module
mymodule.hello()

import datetime
# Date
print(datetime.datetime.now())