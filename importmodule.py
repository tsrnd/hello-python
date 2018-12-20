import module as m
m.printme("Phu")

b = m.person1["age"]
print(b)

c = m.person1["country"]
print(c)


from module import person1
print(person1["age"])