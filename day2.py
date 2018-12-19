from platform import python_version
import time,datetime
print ('Python version', python_version())

print("Here now is :", time.localtime(), "OR ", time.asctime(time.localtime()))
print("UTC now is :", time.gmtime())
print("Time now is :",time.strftime("%H:%M:%S", time.localtime()))

a = [1,"ee", "22", "1", "1"]
b = {1,"ee"}
d = dict()
t = ("a", "b", "c", "1")
b1 = {1,"ee", 1, "ee", "ee"}

print("t = ", t, "sorted t = ",sorted(t))
print("Set b == set b1? ",b == b1)
print("convert list to set ", set(a))
print("union two set ", set(a).union(b))

print("a is ", type(a), "b is ", type(b), "d is ", type(d), "t is ", type(t))

print ('3 / 2 =', 3 / 2)
print ('3 % 2 =', 3 % 2)
print ('3 // 2 =', 3 // 2)
print ('3 / 2.0 =', 3 / 2.0)
print ('3 // 2.0 =', 3 // 2.0)
print ('3 % 2.0 =', 3 % 2.0)

print ("range(3) = ", end='')
for i in range(3):
    print (i, end='')
print()


try:
    a.index(1)
except:
    pass
else:
    print(f"element 1 at {a.index(1)} in a")

try:
    value = d["A"]
except:
    value = None
finally:
    print("Value A in dict d is: ", value)

