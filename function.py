
class Summation(object):
    def sum(self, a, b):
        self.contents = a + b
        print(self.contents)


sumInstance = Summation()
sumInstance.sum(1, 2)

##########


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


myfunc("maitrabm")
# output ['m', 'i', 't', 'r']

#########


def Hello():
    name = input("Enter your name: ")
    if name:
        print("Hello ", name)
    else:
        print("Hello world")
    return


Hello()


#######
