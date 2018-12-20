my_list = [0, 1, 2, 3, 4, 5]
try:
    value = my_list[6]
except IndexError as err:
    print("Error:", err)
else:
    print("Value:", value)


def temp_convert(var):
    try:
        return int(var)
    except ValueError as err:
        print("Error:", err)


print(temp_convert("12!3"))


def raise_exception(n):
    if n < 0:
        raise Exception("Have a error", n)
    return n


try:
    n = raise_exception(-1)
except Exception as err:
    print("Error:", err.args)
else:
    print("N:", n)
