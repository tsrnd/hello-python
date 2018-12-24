import unittest, random
from shell_sort import shellSort
from quick_sort import quickSort


class Testing(unittest.TestCase):
    def testQuickSort(self):
        for _ in range(100):
            list_sort = [random.randint(-100000, 100000) for _ in range(10000)]
            list_copy = list_sort.copy()
            list_copy.sort()
            self.assertEqual(list_copy, quickSort(list_sort))

    def testShellSort(self):
        for _ in range(100):
            list_sort = [random.randint(-100000, 100000) for _ in range(10000)]
            list_copy = list_sort.copy()
            list_copy.sort()
            self.assertEqual(list_copy, shellSort(list_sort))
