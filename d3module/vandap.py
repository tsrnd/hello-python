from d3module import file, number
import os

def sendRequest():
    try:
        chat = file.openFile('./d3module/test/chat.txt', "r+")
    except FileNotFoundError as err:
        chat = file.openFile('./d3module/test/chat.txt', "w+")
        print("FILE NOT EXISTS", err)
    # print(chat.read())
    while (True):
        q = "Dan hoi: day la so nguyen to ah?\n"
        a = ""
        anything = input(q)
        if anything == "0":
            print("bo truong has been left game")
            break
        a = "Bo truong tra loi: Day so %s nguyen to\n" % ("la" if number.checkPrime(int(anything)) else "khong phai")
        if not os.path.exists('./d3module/test/chat.txt'):
            print("chat.txt not exists. we must create it")
        chat.write(q)
        position = chat.tell()
        chat.seek(position+1)
        print(position)
        chat.write(a)
        