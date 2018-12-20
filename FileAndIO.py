import os


def test_keyboard_io():
    print("Hello")
    print("This is keyboard input")
    print("You enter :", input("This is Function input, try enter something: "))
    print("You enter :", eval(
        input("This is Function eval input, try enter something: ")))


# test_keyboard_io


def test_mkdir():
    print("This is File IO:")
    print("Create Fooder")
    os.mkdir("testcreatefooder1")
    os.mkdir("testcreatefooder1/helllo_mkdir.py")
    os.mkdir("testcreatefooder1/testcreatefooder1_1")
    os.mkdir("testcreatefooder1/testcreatefooder1_1/testcreatefooder1_1_1")
    os.mkdir("testcreatefooder1/testcreatefooder1_2")


# test_mkdir()


def test_file_io():
    myFile = open("FileAndIO.txt", "r+")
    print("Hello file : ", myFile.closed)
    for i in range(100):
        myFile.writelines(str(i)+"\n")
    print("data in file : ", myFile.read(10))
    myFile.close()

# test_file_io()


def test_lib_os():
    print("This is path of this file ", os.getcwd())

test_lib_os()
