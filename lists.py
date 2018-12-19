list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# update list
list1[0] = "math"
print("list1[0] after change: ", list1[0])

#del list
del list1[0]
print(list1)