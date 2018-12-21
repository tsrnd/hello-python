
class Summation(object):
    def sum(self, a, b):
        self.contents = a + b
        print(self.contents)

##########


class profile():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Your name is: ", self.name)
        print("Your age is: ", self.age)


############
def myfunc(sequence):
    arr = []
    for x in sequence:
        if x == 'a':
            continue
        if x == "b":
            break
        arr.append(x)
    print(arr)
    return

# output ['m', 'i', 't', 'r']

#########


def Hello():
    name = input("Enter your name: ")
    if name:
        print("Hello ", name)
    else:
        print("Hello world")
    return


#######
