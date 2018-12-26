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

    @pytest.mark.parametrize("salary", [200])
    def test_get_salary(self, salary):
        em = Employee("test", 23, "test")
        em.setSalary(salary)
        get_salary = em.getSalary()
        assert get_salary == ("Salary:", salary)


class TestManager(object):
    @pytest.mark.parametrize(
        "name, age, address, job", [("Na", 23, "DN", "manager")]
    )
    def test_init_manager(self, name, age, address, job):
        mana = Manager(name, age, address, job)
        assert mana.name == name
        assert mana.age == age
        assert mana.address == address
        assert mana.job == job

    @pytest.mark.parametrize(
        "name, age, address, job", [("Na", 23, "DN", "manager")]
    )
    def test_display_manager(self, name, age, address, job):
        mana = Manager(name, age, address, job)
        assert mana.displayManager() == (
            "name is %s and job is %s" % (name, job))
