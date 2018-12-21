# =============================== Example about Functions. ===============================
def funcWithDefaultValue(national='Viet Nam'):
    print('i come from ' + national)
    return

# recursion Function


def recursionFactorial(n):

    try:
        check = int(n)
    except Exception as e:
        raise Exception('It is not digit.')

    if n == 0:
        raise Exception('Can not calculate factorial for 0.')

    if n == 1:
        return 1
    return n*recursionFactorial(n-1)

# Function with more argument.


def moreArguments(name, age, *moreAtt):
    print('Name :', name)
    print('Age :', age)
    for item in moreAtt:
        print('Addition info :', item)
    return

# =============================== Example about Lambda. ===============================


def quadratic_function(a, b, c):
    try:
        testA = int(a)
        testB = int(b)
        testC = int(c)
    except Exception as e:
        raise Exception('input number doesn\'t number. ')
    return lambda x: a*x**2 + b*x+c

# Only Lambda.


def myfunc(n):
    return lambda a: a * n
