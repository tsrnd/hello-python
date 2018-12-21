# tính giai thừa của một số n

def factorial(n):
    if n == 0: return 1
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

print(factorial(8))