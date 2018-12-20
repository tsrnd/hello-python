import os
# Open a file
obj = open("hello.txt", "wb")
print("Name of the file:", obj.name)
print("Close or not:", obj.closed)
print("Opening mode:", obj.mode)
# Close file
obj.close()
# Write filefile
a = open("hello.txt", "w")
a.write("Hello Python")
a.close()
b = open("hello.txt", "r")
str = b.read()
print(str)
# Open file
obj1 = open("hello.txt", "r+")
str1 = obj1.read(10)
print("Read string is:", str1)
# Check current position
pos = obj1.tell()
print("Position file current:", pos)
# Change the file current position
pos1 = obj1.seek(0, 0)
str2 = obj1.read(10)
print("Read again String is:", str2)
print("Position change is", pos1)
# Rename file
os.rename("hello.txt", "world.txt")
# Remove file
os.remove("world.txt")
# Create a directory
os.mkdir("test")
# Remove direction
os.rmdir("test")
