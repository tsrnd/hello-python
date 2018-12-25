import pytest


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def toString(self):
        return self.name + ", " + str(self.age)


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def toString(self):
        return super().toString() + ", " + self.color


def Main():
    pet = Pet("Pet", 1)
    cat = Cat("Tom", 2, "Black")
    print("Is cat is the Pet: " + str(isinstance(cat, Pet)))
    print(cat.toString())


if __name__ == "__main__":
    Main()
