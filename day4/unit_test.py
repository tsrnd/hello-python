import unittest


def sum2(a, b):
    return a + b


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(sum2(2, 3), 5)
