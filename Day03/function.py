def changeme(list):
    list.append(1)
    print(list)
    return
list = [3,2]
print(list)
changeme(list)
print(list)

# Bien cuc bo ghi de
def changeme2(list):
    list = [3,4]
    print(list)
    return
changeme2(list)
print(list)

# Ham co tham so mac dinh
def msg(Id, Name, Age = 18):
    print(Id)
    print(Name)
    print(Age)


msg(Name = "Vu", Id = 211)

# Ham tham so thay doi
def printInfo(a, *b):
    print(a)
    for var in b:
        print(var)
    return

printInfo(3,4,5,2,5)

# Ham nac danh
square = lambda x: x*x
print(square(3))