#!/usr/bin/python
# -*- coding: utf8 -*-
a = 1
b = "b"
c = [1, 2, 3]
d = [1, "2", 3]

# a > 0 và a < 2
print( 0 < a < 2)

#'2' không nằm trong d
print("2" not in d)

#cấu trúc for:
for i in range(0, len(c)):
    print(c[i])
for kt in c:
    print(kt)

i = 0
# cấu trúc while
while i < len(c):
    print(c[i])
    i += 1
