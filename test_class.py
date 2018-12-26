import pytest, class_object

def test_my_class():
    ins = class_object.MyClass()
    assert ins.x == 5

class TestExampleClassObject(object):

    @pytest.mark.parametrize(
        "name, age", [('Haha', 23), ('Hihi', 20)]
    )
    def test_init(self, name, age):
        ps = class_object.Person(name, age)
        assert ps.name == name
        assert ps.age == age

    @pytest.mark.parametrize(
        "name, age", [("Haha", 23)]
    )
    def test_display_person(self, name, age):
        ps = class_object.Person(name, age)
        assert ps.displayPerson() == ("Name:", name, ", Age:", age)
