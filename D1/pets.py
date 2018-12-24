from dog import Dog, Becgiedog, Bulldog


class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())


# my_dogs = [Dog("Tam", 22), Becgiedog("Na", 22), Bulldog("Tram", 22)]

# my_pets = Pets(my_dogs)
# print("I have {} dogs.".format(len(my_pets.dogs)))
# for dog in my_pets.dogs:
#     print("{} is {}.".format(dog.name, dog.age))

# print("And they're all {}s, of course.".format(dog.species))

# tam = Dog("Tam", 22)
# if tam.is_hungry:
#     print("{} is hungry!".format(tam.name))
# else:
#     print("{} isn't hungry!".format(tam.name))

# tam.eat()
# if tam.is_hungry:
#     print("{} is hungry!".format(tam.name))
# else:
#     print("{} isn't hungry!".format(tam.name))

# my_pets.walk()
