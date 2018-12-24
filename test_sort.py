import unittest, random
from sort import *


class Testing(unittest.TestCase):
    max_test_case = 100
    min_range = -100000
    max_range = 100000
    total_number = 10000

    # def selectionSort(self):
    #     for _ in range(self.max_test_case):
    #         case = [random.randint(self.min_range, self.max_range) for _ in range(self.total_number)]
    #         self.assertEqual(sorted(case), selectionSort(case))

    def testBubleSort(self):
        for _ in range(self.max_test_case):
            case = [random.randrange(self.min_range, self.max_range) for _ in range(self.total_number)]
            self.assertEqual(sorted(case), bubleSort(case))
