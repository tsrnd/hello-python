class Parent:
    parentAttr = 100
    def parentMethod(self):
        print ('Goi phuong thuc cua lop cha')
    def __init__(self):
        print ("Call constructor of parent's classs")
    # setter
    def setAttr(self, attr):
        Parent.parentAttr = attr
    # getter
    def getAttr(self):
        print ("Property of parent's class: ", Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print ("Goi constructor cua lop con")
    def childMethod(self):
        print ('Goi phuong thuc cua lop con')

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(96.69)
c.getAttr()

a= 2

if (issubclass(Child, Parent)): print ("true")
else: print ('false')

if (isinstance(c, Parent)): print ('true')
else: print ('false')
    
if (isinstance(a, Parent)): print ('true')
else: print ('false')