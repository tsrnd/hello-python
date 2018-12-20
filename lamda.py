def myfunc(n):
  return lambda a : a * n


mydoubler = myfunc(2)
print(mydoubler(11))

f = open("checknumber.py")
print(f.read(5))
