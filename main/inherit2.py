import pytest


class Parent1(object):
    def __init__(self):
        self.str1 = "Hello"
        print("Parent1")


class Parent2(object):
    def __init__(self):
        self.str2 = "Hi"
        print("Parent2")


class Derived(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        print("Derived")

    def printStr(self):
        print(self.str1, self.str2)


o1 = Derived()
o1.printStr()
