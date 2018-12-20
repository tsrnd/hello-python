import os
x = input("Input :")
print(x)

fo = open("python.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")
fo.close()

fo = open("python.txt", "r+")
str = fo.read(12)
print ("Read String is : ")
print(str)
position = fo.tell()
print ("Current file position : ", position)
str = fo.read()
print ("Read String is : ")
print(str)

print()

position = fo.seek(16, 0)
str = fo.read(10)
print ("Again read String is : ", str)

fo.close()

os.rename("python.txt","python3.txt")
os.remove("python3.txt")