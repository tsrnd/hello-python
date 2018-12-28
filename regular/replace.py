import re

line = "xin chao, toi sinh nam 1996"

formatName = re.sub(r'.*\D', "", line)
print("after remove: %s" % (formatName))

name = 'thai'
age = 22
print(F"Hello {name}, I am {age}")


class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} year olds"


a = A("Thai", 22)

print(f"{a}")
