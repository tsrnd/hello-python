list = [1, "hello", 1.2]
list2 = ["word"]
print list[1:2] + list2
list2.append({"hello":"dd"})
print list2

del list[1]
print list
print list.count("hello")

list3 = [(1,3), (1,2)]
def takeSecond(elem):
    return elem[1]
list3.sort(reverse = True,key = takeSecond)
print list3