n = 10
a = 0
b = 1
for i in range(n):
    a, b = b, a+b
    if b > n:
        break
    print(b, end=' ')
