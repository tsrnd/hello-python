class People:
    'Descreption for class'
    id = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        People.id+=1
    def displayInfo(self):
        print("Name is : %s , age is : %i and id is : %i" %(self.name,self.age,self.id))
    def show(self):
        print("finish")

people1 = People("Nhat",23)
people1.displayInfo()
people2 = People("Den",22)
people2.id = 7
people1.displayInfo()
people2.displayInfo()
print(getattr(people1,"name"))
setattr(people1,"name","Name change")
print(getattr(people1,"name"))
print()
print(People.__doc__)
print(People.__name__)
print(People.__module__)
print(People.__bases__)
print(People.__dict__)

class Nhat(People):
    def displayInfo(self):
        print("--- Name is : %s , age is : %i and id is : %i ---" %(self.name,self.age,People.id))

people3 = Nhat("Nhat",12)
people3.displayInfo()
people3.show()
