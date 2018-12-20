a = [1, 2, 0, 4, 5, 6]
for idx, val in enumerate(a):
    print("Value at %d is: " % idx, val)

print(a[:1]+a[2:])

b = sorted(a, reverse=True)
print(b)

c = [1, 2]
d = [2, 3]
e = c + d
print("E: ", e)
print(list(e))
print(set(e))


def abc(a, b):
    return a > b


a.sort()
a.sort(key=lambda k: k % 2 == 0)
print(a)
