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

# test get type variable
print(type(1))
print(type(""))
print(type(2.2))

# parse kieu du lieu
a = "2"
print(type(int(a)))
b = "2.2"
print(type(float(b)))
c = 222
print(type(str(c)))