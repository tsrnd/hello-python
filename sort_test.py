import unittest
import random
from sort_code import quicksort, insertionsort


def random_array(min_value, max_value, element_number):
    case_test = [random.randint(min_value, max_value)
                 for _ in range(element_number)]
    return case_test


class SortTest(unittest.TestCase):
    case_number = 100

    def testquicksort(self):
        for _ in range(self.case_number):
            case_test = random_array(-100000, 100000, 10000)
            self.assertEqual(sorted(case_test), quicksort(case_test))

    def testinsertionsort(self):
        for _ in range(self.case_number):
            case_test = random_array(-100000, 100000, 10000)
            self.assertEqual(sorted(case_test), insertionsort(case_test))
