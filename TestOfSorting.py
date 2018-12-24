import Sorting as MySorting
import unittest
from random import randint


def initListTest(bound=10_000, rangeStart=-100_000, rangeEnd=100_000):
    return [randint(rangeStart, rangeEnd) for _ in range(bound)]


class TestOfSorting(unittest.TestCase):
    def testMyInsertSort(seft):
        listTest = initListTest()
        seft.assertEqual(MySorting.insertSort(listTest), sorted(listTest))

    def testMyInsertSort(seft):
        listTest = initListTest()
        seft.assertEqual(MySorting.bubleSort(listTest), sorted(listTest))
