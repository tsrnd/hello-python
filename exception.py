import os
try:
    fh = open("testfile", "r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print ("Error: can\'t find file or read data")
else:
    fh.close()
    print ("Written content in the file successfully")

try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print ("Going to close the file")
        fh.close()
        os.remove("testfile")
except IOError:
    print ("Error: can\'t find file or read data")