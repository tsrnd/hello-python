import pytest
# ex1


class Myclass():
    name = "Tram"
    age = 23

    def myfunc(self):
        return ("My age is %d and my name %s" % (self.age, self.name))


# mytest = Myclass()
# print(mytest.myfunc())  # output My age is 23 and my name is Tram


# ex2 _init_ method
class Info(object):
    def __init__(self, address, name, age):
        self.add = address
        self.name = name
        self.age = age

    def display_info(self):
        return ("Your address is %s and your name is %s and your age is %d"
                % (self.add, self.name, self.age))


# your_info = Info("Quang Nam", "Trâm", 23)
# print(your_info.display_info())
# output Your address is Quang Nam and your name is Trâm and your age is 23

# Ex3


class Student(Info):
    def __init__(self, address, name, age, year):
        Info.__init__(self, address, name, age)
        self.year = year

    def get_detail(self):
        return ("Your name is %s and %d years old and is in %s year" %
                (self.name, self.age, self.year))


# student = Student("Dn", "Nguyen Van A", 12, "2014")
# print(student.get_detail())
# output Your name is Nguyen Van A and 12 years old and is in 2014 year
# student.name = "Pham Thi Mai Trâm"
# print(student.get_detail())
# output Your name is Pham Thi Mai Trâm and 12 years old and is in 2014 year


class Multiple(Myclass, Info):
    def __init__(self, add, name, age):
        Myclass.__init__(self)
        Info.__init__(self, add, name, age)


# a = Multiple("QN", "Tr", 23)
# print(a.myfunc())
# print(a.display_info())

# My age is 23 and my name Tr
# Your address is QN and your name is Tr and your age is 23
