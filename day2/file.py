import os

# print to the Screen
print("Hi")

# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()
print ("Closed or not : ", fo.closed)
fo = open("foo.txt", "r+")
str = fo.read(10)
print("Chuoi da doc la : ", str)

position = fo.tell()
print("Con tro file hien tai : ", position)

obj=open("abcd.txt","w")
obj.write("Python xin chao cac ban")
obj.close()
obj1=open("abcd.txt","r")
s=obj1.read()
print(s)
print(len(s))
obj1.close()
obj2=open("abcd.txt","r")
s1=obj2.read(20)
print(s1)
print(len(s1))
obj2.close()

os.rename('abcd.txt', 'abcde.txt')
os.remove('foo.txt')