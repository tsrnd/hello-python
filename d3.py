### define new function

def test(n):
    return [v for v in range(n)]

print(test(7))

#function with default param
def test2(n=7):
    if n == 7:
        print("Wow")
    else:
        print("Oh")

test2(2)

#function with swap param
def test3(p1, p2):
    print("p1 is %s and p2 is %s" % (p1, p2))

test3(p2="P2", p1="P1")

#test function with two param and receive more than two param

def test4(p1, *p2):
    print("Param 1 is %s" % (p1))
    param2s = []
    for v in p2:
        param2s.append(v)
    print("Param 2 is", param2s)

test4("P1", "P2-1", "P2-2", "P2-3", "P2-4")

def test5(*p2, p1):
    print("Param 1 is %s" % (p1))
    param2s = []
    for v in p2:
        param2s.append(v)
    print("Param 2 is", param2s)

test5("P2", "P2-1", p1="Wow")

#test lambda

ld = lambda p=0: print("Wow") if p != 0 else print("Oh?")

# test = lambda a, b: 

ld(7)

n = 7

double = lambda n: pow(n, 2)

print(list(map(double, [1, 2, 3, 4])))

x = filter(lambda x: x%2==0, [1, 2, 3, 4, 5])

print(list(x))

y = [1, 4, 2, 1]

import functools
print(functools.reduce(lambda x, z: x - z + 1, y))
