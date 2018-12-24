import unittest,random
from shell_sort import shellSort,quickSort

# from quick_sort import quickSort


class Testing(unittest.TestCase):
    max_num = 100000
    min_num = -100000
    total_case = 100
    range_array = 10000

    def testQuickSort(self):
        for _ in range(self.total_case):
            list_sort = [random.randint(self.min_num, self.max_num) for _ in range(self.range_array)]
            list_copy = list_sort.copy()
            list_copy.sort()
            self.assertEqual(list_copy, quickSort(list_sort))

    def testShellSort(self):
        for _ in range(self.total_case):
            list_sort = [random.randint(self.min_num, self.max_num) for _ in range(self.range_array)]
            list_copy = list_sort.copy()
            list_copy.sort()
            self.assertEqual(list_copy, shellSort(list_sort))
