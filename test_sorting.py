from Sorting import insertSort, bubleSort
from random import randint


def initListTest(bound=10_000, rangeStart=-100_000, rangeEnd=100_000):
    return [randint(rangeStart, rangeEnd) for _ in range(bound)]


def testMyInsertSort():
    listTest = initListTest()
    assert insertSort(listTest), sorted(listTest)


def testMyBubleSort():
    listTest = initListTest()
    assert bubleSort(listTest), sorted(listTest)
