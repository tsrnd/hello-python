#!/usr/bin/python
# -*- coding: utf8 -*-

numbers = [1,2,3,4,5,6,7,8,9]
names = ["Tuấn", "Nam", "Trường", "Trung"]

#Truy xuất một phần tử của mảng
print(names[1])
print(names[-2])

#số phần tử của list
print(len(names))

#Truy cập mãng an toàn
try:
    name = names[5]
except IndexError:
    print("index out of range")

#kiểm tra phần tử có trong mảng
print("Tuấn" in names)

#trích xuất một mảng con:
a = names[1:3]
a = names[:3]
a = names[2:]
a = names[-2:]

#Xoá phần tử của mảng
del numbers[1]
del numbers[1:3]

#Nối hai mảng:
numbers = [0, 1, 2] + numbers
numbers.append(6)

#lấy phần tử cuối đồng thời xoá nó ra khỏi list
last = numbers.pop()

#Tìm phần tử của list:
try:
    index = names.index("Tuấns")
    print(index)
except Exception:
    print("không tìm thấy")

#Đảo ngược các phần tử của list:
names.reverse()
print(names)

#Sắp xếp list
names.sort()
names.sort(reverse = False)
sorted(names, reverse = False)

#Sắp xếp theo kiểu truyền fuction
def sortNameLen(elem):
    return len(elem)
names.sort(key = sortNameLen, reverse = False)
print(names)