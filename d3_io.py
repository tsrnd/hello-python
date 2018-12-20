import os

# x = input('Input something:')
# print('Input:', x)

# Open file
fo = open("mail.txt", "r+")
print("Name of file:", fo.name)
print("Closed or not:", fo.closed)
print("Opening mode : ", fo.mode)
# fo.write("Hello world!")
content = fo.read(10)
print("Read file:", content)
content = fo.read(10)
print("Read file:", content)
fo.seek(0, 0)
content = fo.read(10)
print("Read file:", content)
fo.close()

# os.rename("mail.txt", "mail1.txt")
