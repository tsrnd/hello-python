abc = input("input here: ")
print(abc)


a = open("day3/abc.txt", "w")
a.write("Hello World")
a.close()

a = open("day3/abc.txt", "r")
b = a.read()
print(b)
a.close()
