#!/usr/bin/python
# -*- coding: utf8 -*-

info = {
    'name': 'Tuấn',
    'tuoi': 28,
    'gioitinh': "Nam"
}

#truy xuất theo key
print(info['name'])

#Thêm một phần tử vào dic
info["diachi"] = 'Vinh Son'
print(info)

#coppy đối tượng
info1 = info.copy()

#Xoá đối tượng
info.clear()
print(info)

info = info1.copy()

keys = ["name", "tuoi", "gt"]
info2 = dict.fromkeys(keys)
print(info2)
info2 = dict.fromkeys(keys, "null")
print(info2)



