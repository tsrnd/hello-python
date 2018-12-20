def fibo(n):
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
        i += 1
    return a


def fibo2(n):
    a, b = 0, 1
    i = 0
    while a < n:
        a, b = b, a + b
        i += 1
    return i
