###list
a = ['1', '2', '3']

for i, v in enumerate(a):
    print("index is %d, value is %s" % (i, v))

# init list with oneline
b = [x for x in range(1, 10)]
print(b)

c = [x for x in range(1, 10) if x % 2 == 0]

print(c)

#del element in list
for i in b:
    if i % 2 != 0:
        del b[b.index(i)]
print("List b after delete some element: ",b)

#add some element in list
b.append("abc")
print("After append:", b)

#reverse list
rev = b[::-1]
print("reverse ok:", rev)

#2D list
d2 = [
    [1, 2, 3],
    [2, 4, 1]
]

print((d2[0] > d2[1]) - (d2[0] < d2[1]))

#insert item inside list
d2.insert(1, [1,1,1])
print("After insert:", d2)
d2.sort(key=lambda l: l[2], reverse=True)

#test abcxyz
b = [1, 2, 3, 4, 3]

###tuple
t = (1, 2, 3, 4, 5, 3)
print("count:", t.count(3))

#create new tuple from two
ct = (1, 2, 3) + (4, 5, 3)
print("compare---:", t == ct)

#sort tuple
xt = [x for x in ct]
xt.sort(reverse=True)
ct = tuple(xt)
print("After sort:", ct)

###dictionary
dic = {
        'a': 3,
        'c': 'c'
    }
dic2 = {
    "a": "x",
    "z": "b",
    "b": "ok",
    "xx": 7,
    "qq": "bb"
}

sorted(dic2, reverse=True)

dic.update(dic2)

print("after update:", dic)

print("abc", dic2.fromkeys({'a', 'b'}, 'good'))

#test update dictionary
ld = [1, 2, 3, 4, 5]
testDic = {i:x for i, x in enumerate(ld)}

print(testDic)
