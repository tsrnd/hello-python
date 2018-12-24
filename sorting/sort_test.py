import random
import unittest
from sorting_algorithm import countingSort, quickSort


def randomArray():
    return [random.randint(-100000, 100000) for _ in range(10000)]


class MyTestSort(unittest.TestCase):
    def testQuickSort(self):
        for _ in range(100):
            array = randomArray()
            sorted_list = sorted(array)
            self.assertEqual(sorted_list, quickSort(array))

    def testCountingSort(self):
        for _ in range(100):
            array = randomArray()
            sorted_list = sorted(array)
            self.assertEqual(sorted_list, countingSort(array))
