import unittest, random

from insertion_sort import insertionSort
from quick_sort import quicksort

def list(min_value, max_value, element_number):
     lists = [random.randint(min_value, max_value)
                  for _ in range(element_number)]
     return lists
    
class TestSort(unittest.TestCase):
    numberTest = 100

    def insertionSortTest(self):
        for _ in range(self.numberTest):
            lists = list(-100000, 100000, 10000)
        self.assertEqual(sorted(lists), insertionSort(lists))

    def quickSortTest(self):
        for _ in range(self.numberTest):
            lists = list(-100000, 100000, 10000)
        self.assertEqual(sorted(lists), quicksort(lists, 0, len(lists) - 1))
