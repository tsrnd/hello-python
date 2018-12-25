class Employee():
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def displayEmployee(self):
        print("Name:", self.name, ",Age:", self.age, ",Address:", self.address)

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, age, address, job):
        Employee.__init__(self, name, age, address)
        self.job = job

    def displayManager(self):
        print("name is %s and job is %s" % (self.name, self.job))


# em1 = Employee("Na", 23, "Da Nang")
# em2 = Employee("Tram", 34, "Quang Nam")
# em1.displayEmployee()
# em2.displayEmployee()

# em = Manager("Tam", 23, "Danang", "manager")
# em.setSalary(300)
# em.getSalary()
# em.displayEmployee()
# em.displayManager()
