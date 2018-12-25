class Employee():
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def displayEmployee(self):
        # return "Name:{},Age:{},Address:{}.".format(self.name, self.age, self.address)
        return ("Name:%s, Age:%s,Address:%s" % (self.name, self.age, self.address))

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, age, address, job):
        Employee.__init__(self, name, age, address)
        self.job = job

    def displayManager(self):
        return("name is %s and job is %s" % (self.name, self.job))


em1 = Employee("Na", 23, "Da Nang")
em2 = Employee("Tram", 34, "Quang Nam")
print(em1.displayEmployee())
print(em2.displayEmployee())

em = Manager("Tam", 23, "Danang", "manager")
print(em.setSalary(300))
print(em.getSalary())
print(em.displayEmployee())
print(em.displayManager())
