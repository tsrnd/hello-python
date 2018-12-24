class Parent:
    def __init__(self):
        print ('Class parent')
    def myMethod(self):
        print ('Call to parent method')
class Child:
    def myMethod(self):
        print ('Call to child method')
c = Child()
c.myMethod()
# p = Parent()
# p.myMethod()