for x in [1,2,3] : print (x,end = ' ')	

list1, list2 = ['C++','Java', 'Python'], [456, 700, 200]
list3 = list1+list2
print ("Max value element : ", max(list1))
print ("Max value element : ", max(list2))
print ("list3 : ".title(), list3)
list3.append(456)
print(list3.count(456))
list3.insert(1,"kotlin")
print(list3)
list2.sort()
print(list2)
list1.reverse()
print(list1)
