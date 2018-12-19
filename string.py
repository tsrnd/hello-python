str1 = "this is string example....wow!!!"
str2 = "3242"
print(str1[3])
print(str1[2:9])
print(str1.capitalize())
print(str1.count("is", 0, len(str1)))
print(str1.find("is", 4, len(str1)))
print(str1.isdigit())
print(str2.isdigit())
print(''.join(str1))
print(str1.split(" ", 3))

for i in range(len(str2)):
    print(str2[i])
