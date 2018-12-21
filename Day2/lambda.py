# Lambda

x = lambda a: -a + 100
print(x(10))

def myLambda(n):
    return lambda a: a * n 

x = myLambda(10)

print(x(10))