
# create and write
def create_file():
    f = open("guangzhou.txt","x")
    f.write("hoang quang chau \nchau hoang quang")
    f.close()

# edit
def read_file(): 
    try:
        f = open("guangzhou.txt", "r")
        print(f.read())
        f.close
    except FileNotFoundError:
        print("Not found")
        create_file()

import os
def del_file():
    os.remove("guangzhou.txt") if os.path.exists("guangzhou.txt") else print("File not found")


read_file()
del_file()

