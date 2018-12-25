import pytest


class Base(object):
    def __init__(self, x):
        self.x = x


class Child(Base):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def printObject(self):
        print(self.x, self.y)


x = Child(5, 7)
x.printObject()

##


class X(object):
    def __init__(self, a):
        self.num = a

    def doubleUp(self):
        self.num *= 2


class Y(X):
    def __init(self, a):
        X.__init__(self, a)

    def trippleUp(self):
        self.num *= 3


yObject = Y(5)
print(yObject.num)

yObject.doubleUp()
print(yObject.num)

yObject.trippleUp()
print(yObject.num)
