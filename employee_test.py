import pytest
from employee import Employee, Manager


class TestEmployee(object):
    @pytest.mark.parametrize(
        "name, age, address", [('Na', 23, 'DN'), ('Tram', 22, 'QN')]
    )
    def test_init(self, name, age, address):
        em = Employee(name, age, address)
        assert em.name == name
        assert em.age == age
        assert em.address == address

    @pytest.mark.parametrize(
        "name,age,address", [("Na", 23, "DN")]
    )
    def test_display_employee(self, name, age, address):
        em = Employee(name, age, address)
        assert em.displayEmployee() == ("Name:%s, Age:%s,Address:%s" %
                                        (name, age, address))
