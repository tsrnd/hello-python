def mercedes(): 
    print("Hello, I'm mercedes car")

def toyota():
    print("Hello, I'm toyota")

class Car:
    def __init__(self, name, color):
        self.name = name
        self.type = type

    def hello(self):
        print("Hello, I'm", self.name)

car = Car("Toyota", "black")
car.hello()