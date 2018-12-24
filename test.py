import unittest, random
from shell_sort import shellSort
from quick_sort import quickSort
class Testing(unittest.TestCase):
    def testQuickSort(self):
        for i in range(100):
            list_sort = []
            for i in range(10000):
                list_sort.append(random.randint(-100000, 100000))
            list_copy = list_sort.copy()
            list_copy.sort()
            self.assertEqual(list_copy,quickSort(list_sort))

    def testShellSort(self):
            for i in range(100):
                list_sort = []
                for i in range(10000):
                    list_sort.append(random.randint(-100000, 100000))
                list_copy = list_sort.copy()
                list_copy.sort()
                self.assertEqual(list_copy,shellSort(list_sort))

