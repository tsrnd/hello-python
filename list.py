ds1 = ["a", "b", "hi", (1, 2), None, True]
print(ds1[:-2])
print(ds1[:4])
print(ds1[3:5])

ds2 = [1, 3, 5, 8, 10, 3]
ds2.append(9)
print(ds2)


list1 = ["a","b"]
list2 = ["c","d"]
list1.append(list2)
print(list1)

list3 = ["a","b"]
# list4 = ["c","d"]
list3.extend(list2)
print(list3)
print(list3[0:3]+list3[2:])
print("a" in list3)

