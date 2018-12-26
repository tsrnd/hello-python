class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayPerson(self):
        return ("Name:", self.name, ", Age:", self.age)

p2 = Person("John", 36)
p2.displayPerson()
print(p2.name)
print(p2.age)
