import unittest
import sort
import random


class SortTest(unittest.TestCase):
    def test_sort(self):
        for _ in range(100):
            list = [random.uniform(-100000,100000) for _ in range(10000)]
            sorted_list = sorted(list)
            list_copy = list.copy()
            assert sort.quick_sort(list_copy, 0, len(list) - 1) == sorted_list
            assert sort.heap_sort(list) == sorted_list
            

