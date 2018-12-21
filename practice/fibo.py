def fib(n):
    a, b = 0, 1
    while a < n:
        print('%d ' %a)
        a, b = b, a+b