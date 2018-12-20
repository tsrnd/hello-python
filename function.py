def changeme1(mylist1):
    print("Inside before change:", mylist1)
    mylist1[2] = 50
    print("Inside after change:", mylist1)


mylist1 = [10, 20, 30]
changeme1(mylist1)
print("Outside:", mylist1)


def changeme2(mylist2):
    mylist2 = [1, 2, 3]
    print("Inside:", mylist2)  # This would assign new reference in mylist2


mylist2 = [10, 20, 30]
changeme2(mylist2)
print("Outside:", mylist2)


def printinfo(val, *vartuple):
    print("--------")
    print(val)
    for i in vartuple:
        print(i)
    return


printinfo(10, 20)

# The return Statement


def sum(arg1, arg2):
    total = arg1+arg2
    print("Inside total:", total)
    return total


total = sum(10, 20)
print("Outside total:", total)
