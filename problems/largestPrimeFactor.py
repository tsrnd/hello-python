# The largest prime factor of the number 600851475143
a = 13195
b = 2
while b < a/2:
    if a % b == 0:
        c = b
        a = a/b
        b = 2
    else:
        b = b + 1
print(int(a))
