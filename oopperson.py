class Person:
    def __init__(self, name, age = 24, gender = "male", height = 172):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
    def showInfo(self):
        print("name", self.name)
        print("Gender: ", self.gender)
        print("age: ", self.age)

    # Tham số age và gender có giá trị mặc định.
    # def __init__ (self, name, age = 1, gender = "Male" ):
         
    #     self.name = name
    #     self.age = age 
    #     self.gender= gender
         
     
    # def showInfo(self):
         
    #     print ("Name: ", self.name)
    #     print ("Age: ", self.age)
    #     print ("Gender: ", self.gender)