import pytest
from class_object import *


def test_my_class():
    ins = Myclass()
    assert ins.myfunc() == "My age is 23 and my name Tram"


class TestInfo(object):
    @pytest.mark.parametrize("address,name,age", [("QN", "Tram", 23)])
    def test_init(self, address, name, age):
        info = Info(address, name, age)
        assert info.address == address
        assert info.age == age
        assert info.name == name
