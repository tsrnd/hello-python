class Animals(object):
    name = ""
    legs = 0

    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
    
    def hello(self):
        print("Hello my name is %s" %(self.name))

class Bird:
    def fly(self):
        print("I can fly")

class Penguin(Animals, Bird): 
    # override from parent
    def fly(self):
        print("I can not fly")

    def hello(self):
        print("I will say hello in my way")

class Fish:
    def swim(self):
        print("I can swim")

penguin = Penguin("Dodo", 2)
penguin.hello()
penguin.fly()
