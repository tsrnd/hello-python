import unittest, random, merge_sort, counting_sort


def randomList(n, begin, end):
    l = []
    for _ in range(n):
        l.append(random.randint(begin, end + 1))
    return l


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        for _ in range(100):
            array = randomList(10000, -100000, 100001)
            arraysort = array[:]
            arraysort.sort()
            self.assertEqual(merge_sort.MergeSort(array), arraysort)


class TestCountingSort(unittest.TestCase):
    def test_counting_sort(self):
        for _ in range(100):
            array = randomList(10000, -100000, 100001)
            arraysort = array[:]
            arraysort.sort()
            self.assertEqual(counting_sort.CountingSort(array), arraysort)
