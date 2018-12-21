class Animal:
    def __init__(self, name, haha = "sfdsf"):
        self.name = name
        self.haha = haha

animal = Animal("duck")
animal.haha = "quangchau"
del animal.haha
animal.haha = "asdsa"
print(animal.haha)
