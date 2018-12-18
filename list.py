mylist = [1, 2, 3]
mylist1 = [2, 3, 4]
aList = ['xyz', 'abc']
# Lay phan tu thu 2 trong mylist
print(mylist[1])
# Lay tu phan tu dau den phan tu 2 trong mylist
print(mylist[:2])
print("-----------------")
# Xoa phan tu thu 1 cua mang
del mylist[0]
print(mylist)
print("--------------")
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
# Vi tri cua phan tu
print("Index for xyz : ", aList.index('xyz'))
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
print("------------------")
value = user.values()
print(value)
