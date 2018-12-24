import unittest
import class_object


class ClassObjectTest(unittest.TestCase):
    def test_count_student(self):
        self.assertEqual(class_object.Student.studentCount, 4)
