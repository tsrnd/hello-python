import pytest
from class_object import *


def test_my_class():
    ins = Myclass()
    assert ins.myfunc() == "My age is 23 and my name Tram"


class TestInfo:
    @pytest.mark.parametrize("address,name,age", [("QN", "Tram", 23)])
    def test_init(self, address, name, age):
        info = Info(address, name, age)
        assert info.add == address
        assert info.age == age
        assert info.name == name

    @pytest.mark.parametrize("address,name,age", [("QN", "Tram", 23)])
    def test_display_info(self, address, name, age):
        info = Info(address, name, age)
        exp = ("Your address is %s and your name is %s and your age is %d" %
               (address, name, age))
        assert info.display_info() == exp


class TestStudent:
    @pytest.mark.parametrize(
        "address,name,age,year", [("QN", "Tram", 23, "2018")]
    )
    def test_init(self, address, name, age, year):
        student = Student(address, name, age, year)
        assert student.add == address
        assert student.name == name
        assert student.age == age
        assert student.year == year

    @pytest.mark.parametrize(
        "address,name,age,year", [("QN", "Tram", 23, "2018")]
    )
    def test_get_detail(self, address, name, age, year):
        student = Student(address, name, age, year)
        expect = ("Your name is %s and %d years old and is in %s year" %
                  (name, age, year))
        assert student.get_detail() == expect


class TestMultiple:
    @pytest.mark.parametrize(
        "add,name,age", [("QN", "Tram", 23)]
    )
    def test_init(self, add, name, age):
        multi = Multiple(add, name, age)
        assert multi.add == add
        assert multi.name == name
        assert multi.age == age
