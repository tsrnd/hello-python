import unittest, random
from quicksort import quickSort
from selectionsort import selectionSort

class Testing(unittest.TestCase):
    const_round = 100
    const_min_random = -100000
    const_max_random = 100000
    const_limit_case = 10000

    #test quicksort with 100 list(10000)
    def testQuickSort(self):
        for _ in range(self.const_round):
          case = [random.randint(self.const_min_random, self.const_max_random) for _ in range(self.const_limit_case)]
          case_copy = case.copy()
          case_copy.sort()
          self.assertEqual(case_copy, quickSort(case,0, self.const_limit_case-1))


    def testSelectionSort(self):
        for _ in range(self.const_round):
          case = [random.randint(self.const_min_random, self.const_max_random) for _ in range(self.const_limit_case)]
          case_copy = case.copy()
          case_copy.sort()
          self.assertEqual(case_copy, selectionSort(case, self.const_limit_case))

            

