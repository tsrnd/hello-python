tuple1 = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
print(tuple1)
tuple2 = 'mon', 'tue', 'wed', 'thu'
print(tuple2)
tuple3 = ()
print(tuple3)
tuple4 = (1,)
print(tuple4)

# constructor tuple
tp1 = tuple([1, "adss", 3])
print(tp1)
print(type(tp1))

# slice
print(tuple1[3:5])
print(tuple1[-2])
print(tuple1[::1])

tuple4 = tuple1
tuple1 = tuple1 + tuple2
print(tuple4)
