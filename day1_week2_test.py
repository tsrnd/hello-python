import pytest
from day1_week2 import ChildMyClass

ch1 = ChildMyClass()
ch2 = ChildMyClass("Ha1-x_")
print(ch1.isMatchRegex(r'^[a-zA-Z0-9\-_]*$'))
print(ch2.isMatchRegex(r'^[a-zA-Z0-9\-_]*$'))

@pytest.mark.parametrize("ch", [ChildMyClass() for _ in range(10)])
def test_child_my_class_random(ch):
    assert ch.isMatchRegex(r'^[a-zA-Z0-9\-_]*$') == True
    assert ch.getPrivateSound() == ch.publicSound[:5]
    ch.setPrivateSound('myprivate')
    assert ch.getPrivateSound() == 'myprivate'
    assert len(ch.randomSound(10)) == 10

def test_child_my_class():
    ch = ChildMyClass("haya_ddd()")
    assert ch.publicSound == "haya_ddd()"
    assert ch.isMatchRegex(r'^[a-zA-Z0-9\-_]*$') == False
