import pytest
from dog import Dog, Bulldog, Becgiedog


class TestDog:
    @pytest.fixture
    def my_dog(self):
        return Dog("Test", 20)

    # test func __init__() of class Dog
    @pytest.mark.parametrize(
        "name, age", [("minh", 23), ("tam", 22), ("na", 21), ("tram", 20)]
    )
    def test_init(self, name, age):
        dog = Dog(name, age)
        assert dog.name == name
        assert dog.age == age
        assert dog.is_hungry == True

    # test func description() of class Dog
    @pytest.mark.parametrize(
        "name, age", [("minh", 23), ("tam", 22), ("na", 21), ("tram", 20)]
    )
    def test_description(self, name, age):
        dog = Dog(name, age)
        assert dog.description() == "{} is {} years old.".format(name, age)

    # test func speak() of class Dog
    @pytest.mark.parametrize("sound", ["Gau gau", "hu hu", "ang ang"])
    def test_speak(self, my_dog, sound):
        my_sound = my_dog.speak(sound)
        assert my_sound == "{} says {}.".format(my_dog.name, sound)

    # test func eat() of class Dog
    def test_eat(self, my_dog):
        my_dog.eat()
        assert my_dog.is_hungry == False

    # test func walk() of class Dog
    def test_walk(self, my_dog):
        assert my_dog.walk() == "{} is walking!".format(my_dog.name)


class TestBulldog:
    @pytest.fixture
    def my_dog(self):
        return Bulldog("Test", 20)

    @pytest.mark.parametrize("speed", ["slowly, quickly"])
    def test_run(self, my_dog, speed):
        assert my_dog.run(speed) == "{} runs {}".format(my_dog.name, speed)


class TestBecgiedog:
    @pytest.fixture
    def my_dog(self):
        return Becgiedog("Test", 20)

    @pytest.mark.parametrize("speed", ["slowly, quickly"])
    def test_run(self, my_dog, speed):
        assert my_dog.run(speed) == "{} runs {}".format(my_dog.name, speed)

