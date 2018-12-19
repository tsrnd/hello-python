#!/usr/bin/python
# -*- coding: utf8 -*-

string1 = "Xin Chao"
string2 = "mai anh tuan"

#Truy xuất một phần tử trong chuổi
print("Truy xuất một phần tử trong chuổi")
print(string1[0])

#truy xuất một đoạn theo range
print("truy xuất một đoạn theo range")
print(string1[1: 3])
print(string1[1: -2])
print(string1[:3])
print(string1[5:])
print(string1[:-3])

#ghi trên nhiều dòng
string3 = """ dong 1
dong 2
dong 3
dong 4"""
# nối chuổi
string4 = string1 + " " + string2

# độ dài chuổi
dodai1 = len(string1)

#tìm, thay thế nội dung
string1 = string1.replace("Chao", "chao")

#tim tu trai qua phai
index = string2.find("tuan")

#tim tu phai qua trai
index2 = string2.rfind("a")

#tách chuổi thành list
string2s = string2.split()
print(string2s)
string2ss = string2.split(" ")

#tách theo dòng
string3s = string3.splitlines()

#trim chuổi
string11 = string1.strip("X")
print(string11)
#trim trái
string11 = string1.lstrip()
#trim phải
string11 = string1.rstrip()

#join mang string2.split() thanh chuổi cách nhau giấu --
string22 = "--".join(string2.split())
print(string22)

#bản sao của chuổi với chữ cái đầu được viết hoa
string22 = string2.capitalize()