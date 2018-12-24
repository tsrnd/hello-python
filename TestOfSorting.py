import Sorting as MySorting
import unittest
from random import shuffle, randint


def initListTest(testCases, bound=10_000, rangeStart=-100_000, rangeEnd=100_000):
    listTestCase = []
    for _ in range(testCases):
        temp = []
        for _ in range(bound):
            temp.append(randint(rangeStart, rangeEnd))
        listTestCase.append(temp)
    return listTestCase


class TestOfSorting(unittest.TestCase):
    def testMyInsertSort(seft):
        numOfTestCase = 100
        listTest = initListTest(numOfTestCase)
        for i in range(numOfTestCase):
            print("Progress of testMyInsertSort: {} / {} %".format(i+1,numOfTestCase))
            seft.assertEqual(MySorting.insertSort(
                listTest[i]), sorted(listTest[i]))

    def testMyBubbleSort(seft):
        numOfTestCase = 100
        listTest = initListTest(numOfTestCase)
        for i in range(numOfTestCase):
            print("Progress of testMyBubbleSort: {} / {} %".format(i+1),numOfTestCase)
            seft.assertEqual(MySorting.bubleSort(
                listTest[i]), sorted(listTest[i]))


if __name__ == "__main__":
    unittest.main()
