import unittest
import pack1.subpack1.subsubpack1.module1 as mymodule1
import pytest



def sum(x, y):
    return x + y

class MyTest(unittest.TestCase):
    def testSum(self):
        self.assertEqual(sum(3,1), 4)
    def testnCk(self):
        self.assertIsNotNone(mymodule1.nCk(3,2))
        self.assertTrue(len(mymodule1.nCk(3,2)) == 3)
        assert len(mymodule1.nCk(3,2)) == 3


if __name__ == "__main__":
    unittest.main()