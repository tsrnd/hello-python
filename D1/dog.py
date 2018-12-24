class Dog:
    # class attribute
    species = "mammal"

    # initilizer
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # instance method
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}.".format(self.name, sound)

    # instance method
    def eat(self):
        self.is_hungry = False

    # instance method
    def walk(self):
        return "{} is walking!".format(self.name)


class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


class Becgiedog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# duc = Dog("Đực", 3)
# print(duc.description())
# print(duc.speak("Gâu gâu!"))
# print(isinstance(duc, Dog))

# den = Bulldog("Den", 1)
# print(den.description())
# print(duc.speak("Ẳng ẳng!"))
# print(isinstance(den, Dog))
# print(isinstance(den, Bulldog))
# print(isinstance(den, Becgiedog))
