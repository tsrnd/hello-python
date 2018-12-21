class Player:
    minAge = 18
    maxAge = 100
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def showInfo(self):
        print("name", self.name)
        print("age", self.age)
    def __del__(self):
        del self.name,self.age
        print(" destruct done")