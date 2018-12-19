mylist = [1, 2, 3]
mylist1 = [2, 3, 4]
aList = ['xyz', 'abc']
aList[1] = 'axb'
# Thay doi 1 gia tri cua list cu the
print(aList)
# Do dai cua mang
print(len(aList))
# Chen 1 muc lam vi tri thu 2
aList.insert(1, 'sdad')
print(aList)
# Loai bo muc duoc chi dinh
aList.remove('sdad')
print(aList)
# Lay phan tu thu 2 trong mylist
print(mylist[1])
# Lay tu phan tu dau den phan tu 2
print(aList[:1])
print("-----------------")
# Xoa phan tu thu 1 cua mang
del aList[0]
print(aList)
print("--------------")
# Xoa phan tu cuoi cung
print(mylist.pop())
print(mylist)
# Xoa trong list
print(mylist.clear())
#
thislist = list(("a", "b", "c"))
print(thislist)
# Cong 2 mang
print(mylist + mylist1)
print("----------------")
# Them phan tu vao mang
mylist.append(5)
print(mylist)
print("----------------")
# Xoa phan tu cuoi cung
mynumber = mylist.pop()
print(mynumber)
print(mylist)
print("-----------------")
# # Vi tri cua phan tu
# print("Index for xyz : ", aList.index('xyz'))
print("------------------")
# Dao nguoc vi tri cua mang
mylist.reverse()
print(mylist)
# Sap xep gia tri phan tu
aList.sort()
print("List: ", aList)
# Them 1 phan tu
user = {'name': 'Jone', 'age': 23}
user['country'] = 'Vietnam'
print(user)
