import pytest


class Pet:
    pass


class Dog(Pet):
    pass


a = Pet()
b = Dog()
print("Dog is a subclass of Pet: ", issubclass(Dog, Pet))
print("b is a instancell of Pet: ", isinstance(b, Pet))
