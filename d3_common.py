# print info
def print_info(name, age):
    print("Name:", name)
    print("Age:", age)
    return


# factorial
def factorial(n):
    if n == 0:
        return 1
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def devide(x, y):
    if y == 0:
        raise ValueError("Can not devide by zero!")
    return x / y
