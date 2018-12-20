# syntax
def printme(param):
    print(param)
    return


printme("lgtm")


# pass by referrence vs value
# all param(arg) in the python language are passed by reference
def printme2(list):
    print("Before change:", list)
    list[0] = 100
    print("After change:", list)
    return


my_list = [1, 2, 3, 4, 5]
printme2(my_list)
print("My list:", my_list)


def printme3(list):
    list = ["a", "b", "c"]  # assign new reference in list
    print("List character:", list)
    return


printme3(my_list)
print("My list:", my_list)


# default arguments
def printinfo(name, age=23):
    print("Name:", name)
    print("Age:", age)
    return


printinfo("Minh")


# variable-length arguments
def printinfo2(arg1, *vartuple):
    print("1:", arg1)
    for var in vartuple:
        print("vartuple:", var)
    return


printinfo2(23, "Dao", "Thanh", "Minh")

# anonymous funtions
sum = lambda a, b: a + b
print(sum(1, 2))
