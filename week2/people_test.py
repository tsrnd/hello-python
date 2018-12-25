import pytest
from classes import People


class TestPeople:
    @pytest.mark.parametrize("name, age", [("hoa", 20), ("hanh", 21)])
    def test_init(self, name, age):
        people = People(name, age)
        assert people.name == name
        assert people.age == age

    @pytest.mark.parametrize("name, age", [("abc", 20), ("def", 30)])
    def test_display(self, name, age):
        people = People(name, age)
        assert people.display_people() == "People is {} and {} ages".format(name, age)
