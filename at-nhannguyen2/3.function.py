def changelist(mylist):
    mylist[0] = 10
    return


mylist = [1, 2, 3, 4, 5]
# list after change
changelist(mylist)

print(mylist)


def changelist2(mylist):
    mylist = [1, 2, 3, 4]
    print(mylist)
    return


mylist2 = [1, 2, 3, 4, 5]
# list not change
changelist2(mylist2)

print(mylist2)

# lambda
mul = lambda a, b: a * b

print(mul(2, 4))


def printinfo(name, age):
    print("Name: %s, Age: %s" % (name, age))
    return


# printinfo keyword agrument
printinfo(name="nguyen nhan", age=23)
printinfo(age=23, name="nguyennhan")


def printlist(a, *b):
    print(a)

    for i in b:
        print(i)
    return


# multi agrument
printlist(
    1,
    2,
    5,
    7,
)
