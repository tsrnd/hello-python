import Sorting as MySorting
import unittest
from random import shuffle


class TestOfSorting(unittest.TestCase):
    def testMyInsertSort(seft):
        limit = 10_000
        expecta = []
        actual = []
        for i in range(limit):
            expecta.append(i)
            actual.append(i)
        shuffle(actual)
        seft.assertEqual(MySorting.insertSort(actual), expecta)

    def testMyBubbleSort(seft):
        limit = 10_000
        expecta = []
        actual = []
        for i in range(limit):
            expecta.append(i)
            actual.append(i)
        shuffle(actual)
        seft.assertEqual(MySorting.bubleSort(actual), expecta)


if __name__ == "__main__":
    unittest.main()
