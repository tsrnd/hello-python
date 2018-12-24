import unittest
import random

from sort_exercise import countingSort, quickSort


class testSort(unittest.TestCase):
    def testCountingSort(self):
        for _ in range(100):
            case_test = [random.randint(-100000, 100000) for _ in range(10000)]
            case_copy = case_test.copy()
            case_copy.sort()
            self.assertEqual(case_copy,  countingSort(case_test))

    def testQuickSort(self):
        for _ in range(100):
            case_test = [random.randint(-100000, 100000) for _ in range(10000)]
            case_copy = case_test.copy()
            case_copy.sort()
            self.assertEqual(case_copy,  quickSort(case_test))
