import unittest, random
from sort import *

class Testing(unittest.TestCase):
    max_test_case = 5
    min_range = -100000
    max_range = 100000
    total_number = 10000

    # def testBubleSort(self):
    #     for _ in range(self.max_test_case):
    #         case = [random.randint(self.min_range, self.max_range) for _ in range(self.total_number)]
    #         case_copy = case.copy()
    #         sorted(case_copy)
    #         self.assertEqual(case_copy, bubleSort(case))

    def testSelectionSort(self):
        for _ in range(self.max_test_case):
            case = [random.randint(self.min_range, self.max_range) for _ in range(self.total_number)]
            case_copy = case.copy()
            sorted(case_copy)
            self.assertEqual(case_copy, selectionSort(case))
