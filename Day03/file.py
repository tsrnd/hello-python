# str = input("Input: ")
# print(str)
# str = raw_input("Input: ")
# print(str)

import os

# Mo mot file
fo = open("foo.txt", "w")
fo.write( "Python la mot ngon ngu lap trinh tuyet voi.\n Toi la Ngoc Vu.\n")
fo.close()
fo = open("foo.txt", "r")
for line in fo:
    print(line, end='')
# Dong file da mo
fo.close()

os.rename("foo.txt", "foo2.txt")

# Mo mot file
fo = open("foo2.txt", "r+")
str = fo.read(10)
print ("Chuoi da doc la : ", str)

# Kiem tra con tro hien tai
position = fo.tell()
print ("Con tro file hien tai : ", position)

# Dat lai vi tri con tro tai vi tri ban dau mot lan nua
position = fo.seek(0, 0)
str = fo.read(10)
print ("Chuoi da doc la : ", str)
# Dong file da mo
fo.close()