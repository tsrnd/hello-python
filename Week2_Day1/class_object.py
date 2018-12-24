class Student:
    # Variable class
    studentCount = 0

    def __init__(self, name, point):
        self.name = name
        self.point = point
        Student.studentCount += 1
        print("Khoi tao doi tuong Student")

    def __del__(self):
        print("Destroy")

    def getStudentCount(self):
        return Student.studentCount

    def displayStudent(self):
        print("Name : {0} || Point : {1}" . format(self.name, self.point))

    def getName(self):
        print("Name of student: {0}".format(self.name))


st1 = Student("Vu", 10)
print(st1.getStudentCount())

st2 = Student("Ha", 30)
print(Student.studentCount)

st1.displayStudent()

print("Student.__doc__:", Student.__doc__)
print("Student.__name__:", Student.__name__)
print("Student.__module__:", Student.__module__)
print("Student.__bases__:", Student.__bases__)
print("Student.__dict__:", Student.__dict__)
print(id(st1))
print(id(st2))
del st2
st3 = st1
st4 = Student("Minh", 22)
print(id(st4))
print(id(st3))


class Member(Student):
    __IQ = 0  # private variable

    def __init__(self, name, point):
        super().__init__(name, point)
        print("Khoi tao lop {0}".format(Member.__name__))

    # Override function
    def getName(self):
        print("Name of member: {0}".format(self.name))

    def getIQ(self):
        return self.__IQ


mb1 = Member("Truong", 11)
mb1.displayStudent()
mb1.getName()
print(mb1.getIQ())
