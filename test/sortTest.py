import random
import unittest
import introsort
import timsort


class testSort(unittest.TestCase):
    def testTimSort(self):
        for _ in range(100):
            arr = [random.uniform(-100000, 100000) for _ in range(10)]
            n = len(arr)

            b = arr.copy()
            b.sort()
            self.assertEqual(b,  timsort.timSort(arr, n))

    def testIntroSort(self):
        for _ in range(100):
            a = [random.uniform(-100000, 100000) for _ in range(10000)]
            b = a.copy()
            b.sort()
            self.assertEqual(b,  introsort.introSort(a, 2))
