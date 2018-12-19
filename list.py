# slice
ds1 = ["a", "b", "hi", (1, 2), None, True]
print(ds1[:-2])
print(ds1[:4])
print(ds1[3:5])

ds2 = [1, 3, 5, 8, 10, 3]
ds2.append(9)
print(ds2)
print("----------------------")

list1 = ["a", "b"]
list2 = ["c", "d"]
list1.append(list2)
print(list1)

list3 = ["a", "b"]
# list4 = ["c","d"]
list3.extend(list2)
print(list3)
print(list3[0:3]+list3[2:])
print("a" in list3)
print("----------------------")

# list tham chieu
l1 = [1, 3, 5, 6, 2, 5]
l2 = l1
l3 = l1[:]
l1[0] = 10
print(l1)
print(l2)
print(l3)
print("----------------------")

a = []
b = []
c = []
b.append(1)
b.append(2)
c.append(3)
a.append(c)
a.extend(b)
print(a)
