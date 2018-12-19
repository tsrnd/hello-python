# multiple assignment
a = b = c = 1
print("a =", a, ", b = ", b, ", c = ", c)

a, b, c = 1, 2, "minh"
print("a =", a, ", b = ", b, ", c = ", c)

# =================string=================
str = "Hello world!"
print(str)
print(str[1])
print(str[2:5])
print(str[2:])
print(str*2)
print(str[-1])
print(str[:-1])
print(str+"concatenate")

# =================list=================
list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list_1)
list_2 = ["a", "b", "c", 18, 8, 95, True, (18, 8, 95)]
print(list_2)
print(list_2[-1])
print(list_1[2:5])  # from index 2 to before 5
print(list_1[2:])  # from index 2 -> end
print(list_1[-5:])  # from index -5 -> end
print(list_1[:-5])  # from start -> before -5
print(list_1[2::3])  # jump 3 from index 2
print(list_1[::-1])  # revert list

list_1.append(10)  # add element after last index
print(list_1)

list_1.insert(2, 69)  # add element to index 2
print(list_1)

pop_var = list_1.pop()  # delete last element and assign it to varibale
print(pop_var)
print(list_1)

list_1.remove(69)  # remove first element = 69, exception ValueError
print(list_1)

# copy list
list_3 = [1, 2, 3, 4]

'''
list_4 chỉ sao chép tham chiếu chứ ko tạo danh sách thực
nếu list_3 thay đổi thì list_4 thay đổi
'''
list_4 = list_3
print(list_3 is list_4)

'''
list_5, list_6, list_7 là danh sách mới, độc lập
list_3 thay đổi thì cũng ko ảnh hưởng 
'''
list_5 = list_3[:]
print(list_3 is list_5)

list_6 = list_3.copy()
print(list_3 is list_6)

list_7 = list(list_3)
print(list_3 is list_7)

# extend list
list_8 = list_5 + list_6
print(list_8)
list_5.extend(list_6)
print(list_5)
print(len(list_8))

# =================tuple=================
days = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
print(days)
print(days[3:6])
free = ()  # empty tuple
print(free)
days_new = tuple(['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
print(days_new)

# =================dict=================
profile = {'Name': 'Minh', 'Age': 23, 'Class': 'Python'}
print("profile['Name']: ", profile['Name'])  # exception KeyError
print("profile['Age']: ", profile['Age'])
profile['Relationship'] = "Single"
print("profile['Relationship']:", profile['Relationship'])
profile.clear()
print(profile)
del profile

print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(()))

# =================set=================
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6}
print(set_1)
print(set_1 - set_2)  # hiệu
print(set_2 - set_1)
set_3 = set('hello')
print(set_3)

set_2.add(7)
print(set_2)

print(set_1 & set_2)  # giao
print(set_1 | set_2)  # hợp
print(set_1 ^ set_2)  # hiệu đối xứng
print(set_1 >= set_2)  # kiểm tra bên trái có là cha bên phải
print(set_1 <= set_2)  # kiểm tra bên phải có là cha bên trái
print(1 in set_1)  # kiểm tra sự tồn tại của phần tử
