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

            # Sorting implement.
            b.sort()
            timsort.timSort(arr, n)

            self.assertEqual(b, arr)

    def testIntroSort(self):
        for _ in range(100):
            a = [random.uniform(-100000, 100000) for _ in range(10)]
            b = a.copy()

            # Sorting implement.
            b.sort()
            introsort.introSort(a)

            self.assertEqual(b,  a)
