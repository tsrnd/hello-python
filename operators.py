# Operators
print(10 + 5)  # result 15
print("tram" + " pham")  # result tram pham
print(10 - 5)  # result 5
print(10 * 5)  # result 50
print("tram" * 5)  # result tramtramtramtramtram
print(10/5)  # result 2.0
print(10 % 5)  # result 0
print(10 // 5)  # result 2 #floor devision
print(11//2)  # result 5   #floor devision
print(15 // -4)  # result -4
print(10 ** 5)  # result 100000 (=10^5)

# Comparison Operators
a = 10
b = 5
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")  # a != b
if a > b:
    print("a is more than b")
else:
    print("a is less than b")  # a < b
if a >= b:
    print("a is more than or equal to b")
else:
    print("a is less than b")  # a < b
if a <= b:
    print("a is less than or equal to b")
else:
    print("a is more than b")  # a > b

# Assignment Operators
a = 10
b = 2
c = 1
c = a + b
print("c =", c)  # c=12
c += a
print("c =", c)  # c=22
c *= b
print("c =", c)  # c=44
c /= b
print("c =", c)  # c=22.0
c %= a
print("c =", c)  # c=2.0
c = 10
c **= b
print("c =", c)  # c=100
c //= a
print("c =", c)  # c=10
c -= b
print("c =", c)  # c=8

# Logical operators
x = True
y = False
print(a and y)  # False
print(x or y)  # True
print(not x)  # Flase

# Bitwise operators
x = 10  # 00001010
y = 2   # 00000010
print(x & y)  # result 2 (00000010)
print(x | y)  # result 10 (00001010)
print(~15)  # result -16 (-(x+1))
print(x ^ y)  # result 8 (00001000) (XOR)
print(x >> 3)  # result 1 (00001) Bitwise right shift
print(x >> 2)  # result 2 (000010) Bitwise right shift
print(x << 2)  # result 40 (0000101000) Bitwise left shift

# Identity operators
x = 1
y = 1
z = "1"
print(x is y)  # True
print(x is not y)  # False
print(x is z)  # False

# Membership operators
x = "python"
y = {1: "a", 2: "b"}
print('y' in x)  # True
print('Y' in x)  # False
print(1 in y)  # True
print('a' in y)  # False
print('a' in y.values())  # True
print(3 not in y.keys())  # True
