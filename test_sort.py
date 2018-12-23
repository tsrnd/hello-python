import unittest
import random

from sort_exercise import gnomeSort, oldEventSort


class testSort(unittest.TestCase):
    def testGnomeSort(self):
        for _ in range(100):
            case_test = [random.randint(-100000, 100000) for _ in range(10000)]
            case_copy = case_test.copy()
            case_copy.sort()
            self.assertEqual(case_copy,  gnomeSort(case_test))

    def testOldEvenSort(self):
        for _ in range(100):
            case_test = [random.randint(-100000, 100000) for _ in range(10000)]
            case_copy = case_test.copy()
            case_copy.sort()
            self.assertEqual(case_copy,  oldEventSort(case_test))
