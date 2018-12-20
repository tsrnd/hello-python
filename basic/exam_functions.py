# =============================== Example about Functions. ===============================
def funcWithDefaultValue(national='Viet Nam'):
    print('i come from ' + national)


str = input()
if len(str) > 0:
    funcWithDefaultValue(str)
else:
    funcWithDefaultValue()


def recursionFactorial(n):
    if n == 1:
        return 1
    return n*recursionFactorial(n-1)


# print(recursionFactorial(4))

# =============================== Example about Lambda. ===============================
def quadratic_function(a, b, c):
    return lambda x: a*x**2 + b*x+c
fx = quadratic_function(1, 2, 3)
print(fx(2))

# Only Lambda.
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(5)
print(mydoubler(11))