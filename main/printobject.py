import pytest


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "From str: a is %s, b is %s" % (self.a, self.b)

    def __str__(self):
        return "From repr: a is %s," \
               "b is %s" % (self.a, self.b)


a = A("thai", "le")
print(a)
print([a])
