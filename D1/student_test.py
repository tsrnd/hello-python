import pytest
from student import Student


@pytest.mark.parametrize(
    "name, age, name_expect, age_expect",
    [
        ("minh", 23, "minh", 23),
        ("tam", 22, "tam", 22),
        ("na", 21, "na", 21),
        ("tram", 20, "tram", 20),
    ],
)
def test_student_init(name, age, name_expect, age_expect):
    student = Student(name, age)
    assert name == student.name
    assert age == student.age


@pytest.mark.parametrize(
    "name, age", [("minh", 23), ("tam", 22), ("na", 21), ("tram", 20)]
)
def test_student_display(name, age):
    student = Student(name, age)
    assert "Name: {}, Age: {}".format(name, age) == student.display()
