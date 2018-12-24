import Sorting as MySorting
import unittest
import pytest
from random import randint


def initListTest(bound=10000, rangeStart=-100000, rangeEnd=100000):
    return [randint(rangeStart, rangeEnd) for _ in range(bound)]


class TestOfSorting(unittest.TestCase):
    def testMyInsertSort(seft):
        listTest = initListTest()
        seft.assertEqual(MySorting.insertSort(listTest), sorted(listTest))

    def testMyInsertSort(seft):
        listTest = initListTest()
        seft.assertEqual(MySorting.bubleSort(listTest), sorted(listTest))


if __name__ == "__main__":
    unittest.main()
