# define variable
a = 2  # type int
b = "ab\nc"  # type string
c = 1.1  # type float
d = complex(1, 2)  # complex
e = r'ab\nc'  # raw_string

# print variable
print(a, b)
print(b + "addtext")
print("phần thực", d.real)
print("phần ảo", d.imag)
print(e + "addtext")
# check type variable
print(type(b))
print(type(a))
print(type(str(a)))
# bool
print(bool('true'))
# convert type
print(str(a))
print(int(c))

# list
ls1 = ["a", "b", 2, "d"]
ls2 = [1, 2, 3]
print(ls1 + ls2)
del ls2[2]
print(ls2)
print(ls2 * 2)
print(ls1[:1])
print(ls1[1:3])
ls1.append(["add", "add2"])
print(ls1)
ls1.extend(["add", "add2"])
print(ls1)
ls2[1] = 100
print(ls2)

# tuples
tp1 = (1, "a", 1.1, "b")  # tuples
tp2 = ("e", "g", "h")
print(tp1[1:3])
print(tp1 + tp2)
print(tp1 * 5)
print(tp1 + (4, 5))

# add or replace tuples
ls3 = list(tp1)
ls3[1] = 1000
ls3.append("123")
tp3 = tuple(ls3)
print(tp3)
tp4 = tp3 + (8, 9)
print(tp4)

# dictionary
dict = {}
dict[1] = "one"
print(dict[1])
dict['second'] = "second"
print(dict)
print(dict.keys())
print(dict.values())
