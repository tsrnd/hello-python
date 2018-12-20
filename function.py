def sum(a, b):
    total = a + b
    print("Tong 2 so la:", total)
    return total


sum(5, 10)


def printme(str):
    print(str)


printme("Hello Na")


def changeme(mylist):
    mylist = [1, 2, 3]
    print("Cac gia tri ben trong ham:", mylist)
    return


mylist = [6, 7, 8]
changeme(mylist)
print("Cac gia tri ngoai ham:", mylist)

name = "Na"


def msg():
    age = 23
    print("Ten cua toi:", name)
    print("Tuoi cua toi :", age)


msg()
