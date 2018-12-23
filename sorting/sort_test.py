import random
import pytest
import unittest
from sorting_algorithm import gnomeSort, quickSort


def randomArray():
    array = []
    for _ in range(10000):
        array.append(random.randint(-100000, 100000))
    return array


class MyTestSort(unittest.TestCase):
    def testQuickSort(self):
        for _ in range(100):
            array = randomArray()
            sorted_list = sorted(array)
            assert sorted_list == quickSort(array)

    def testGnomeSort(self):
        for _ in range(100):
            array = randomArray()
            sorted_list = sorted(array)
            assert sorted_list == gnomeSort(array)


if __name__ == "__main__":
    unittest.main()
