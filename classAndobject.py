# ex1
class Myclass():
    name = "Tram"
    age = 23

    def myfunc(self):
        print("My age is %d and my name %s" % (self.age, self.name))


mytest = Myclass()
mytest.myfunc()  # output My age is 23 and my name is Tram


# ex2 _init_ method
class Info(object):
    def __init__(self, address, name, age):
        self.add = address
        self.name = name
        self.age = age

    def display_info(self):
        print("Your address is", self.add)
        print("Your name is", self.name)
        print("Your age is", self.age)


your_info = Info("Quang Nam", "Trâm", 23)
your_info.display_info()
# output
# Your address is Quang Nam
# Your name is Trâm
# Your age is 23

# Ex3


class Student(Info):
    def __init__(self, address, name, age, year):
        Info.__init__(self, address, name, age)
        self.year = year

    def get_detail(self):
        print("Your name is %s and %d years old and is in %s year" %
              (self.name, self.age, self.year))


student = Student("Dn", "Nguyen Van A", 12, "2014")
student.get_detail()
# output Your name is Nguyen Van A and 12 years old and is in 2014 year
student.name = "Pham Thi Mai Trâm"
student.get_detail()
# output Your name is Pham Thi Mai Trâm and 12 years old and is in 2014 year


class Multiple(Myclass, Info):
    def __init__(self, add, name, age):
        Myclass.__init__(self)
        Info.__init__(self, add, name, age)


a = Multiple("QN", "Tr", 23)
a.myfunc()
a.display_info()

# My age is 23 and my name Tr
# Your address is QN
# Your name is Tr
# Your age is 23
