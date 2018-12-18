#variable

test = "abc"
print(test)

num = 7
c = 0

for i in range(1, num + 1):
    if num % i == 0:
        c += 1

print(c)

rs = True if c == 2 else False

print(rs)