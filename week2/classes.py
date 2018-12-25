class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_people(self):
        return "People is {} and {} ages".format(self.name, self.age)
