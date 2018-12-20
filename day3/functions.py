def sum_2_number(a, b):
    return a + b


print("sum 2 & 3 is: ", sum_2_number(2, 3))


def printAll(a, *b):
    print(a)
    for c in b:
        print(c)


printAll(1, 2, 3)


def square(a): return a * a


print("Square of 10 is: ", square(10))
