import unittest, random, sort

def randomList(n, begin, end):
    l = []
    for _ in range(n):
        l.append(random.uniform(begin, end + 1))
    return l

class TestshellSort(unittest.TestCase):
    def test_shellSort(self):
        for _ in range(100):
            array = randomList(10000, -100000, 100000)
            arraysort = array.copy()
            arraysort.sort()
            self.assertEqual(sort.shellSort(array), arraysort)

class TestQuickSort(unittest.TestCase):
    def test_quickSort(self):
        for _ in range(100):
            array = randomList(10000, -100000, 100000)
            arraysort = array.copy()
            arraysort.sort()
            self.assertEqual(sort.quickSort(array), arraysort)
