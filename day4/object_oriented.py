class People:
    __abc = 'abc'

    def __init__(self, name):
        self.name = name

    def displayName(self):
        print("Name is: ", self.name)


class Student(People):
    def __init__(self, name, clazz):
        super().__init__(name)
        self.clazz = clazz

    def __displayClazz(self):
        print("Clazz is: ", self.clazz)


student = Student("Hoa", 10)
student.displayName()
student._Student__displayClazz()
print(People._People__abc)
