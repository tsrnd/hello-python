import unittest, random, sort

def randomList(n, begin, end):
    l = []
    for _ in range(n):
        l.append(random.randint(begin, end + 1))
    return l

class TestInsertionSort(unittest.TestCase):
    def test_insertionSort(self):
        for _ in range(100):
            array = randomList(10000, -100000, 100000)
            arraysort = array.copy()
            arraysort.sort()
            self.assertEqual(sort.insertionSort(array), arraysort)

class TestQuickSort(unittest.TestCase):
    def test_quickSort(self):
        for _ in range(100):
            array = randomList(10000, -100000, 100000)
            arraysort = array.copy()
            arraysort.sort()
            self.assertEqual(sort.quickSort(array), arraysort)
