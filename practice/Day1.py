class D(object):
    multiplier = 2

    @classmethod
    def f(cls, x):
        return cls.multiplier * x
    
    def h(self, x):
        return self.multiplier * x

    @staticmethod
    def g(name):
        print("Hello, %s" % name)

# print(D.f(23))
# print(D.g("Tanh"))

# d = D()
# d.multiplier = 12
# print(d.h(2))
# print(D.multiplier)

class Rectangle():
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return (self.w + self.h) * 2

class Square(Rectangle):
    def __init__(self, s):
        super().__init__(s, s)
        self.s = s

r = Rectangle(3, 4)
print(r.area())
print(r.perimeter())
s = Square(3)
print(s.area())
