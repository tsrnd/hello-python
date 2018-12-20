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

print(max(list2))
print(min(list2))

# converts to list
aTuple = (123, 'C++', 'Java', 'Python')
list1 = list(aTuple)
print ("List elements : ", list1)

str = "Hello World"

list2 = list(str)
print ("List elements : ", list2)

# append
list2.append("!!!!")
print(list2)

# count
print(list2.count("o"))

# extend
list2.extend(list3)
print(list2)

# index: return index of obj
print(list1.index(123))

# insert the given element at the given index
list1.insert(1, 'abc')
print(list1)

# pop() remove laster obj from the list or which index given
list1.pop()
list1.pop(1)
print(list1)

# remove() remove object which is given
list1.remove('Java')
print(list1)

# reverse()
list1.reverse()
print(list1)

# Multi-Dimensional List
List = [['Hi', 'Hello'], ['Bye']]

print(List[0][1])
print(List[1][0])

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks'] 

print(List[-1])
print(List[-3])

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
List.remove(5) 
List.remove(6) 
print(List)


List.pop() # remove the last element
print(List)

