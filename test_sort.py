import unittest
import random

from sort_exercise import gnomeSort, oldEventSort


class testSort(unittest.TestCase):
    def testGnomeSort(self):
        for _ in range(100):
            a = [random.randint(-100000, 100000) for _ in range(10000)]
            b = a.copy()
            b.sort()
            self.assertEqual(b,  gnomeSort(a))

    def testOldEvenSort(self):
        for _ in range(100):
            a = [random.randint(-100000, 100000) for _ in range(10000)]
            b = a.copy()
            b.sort()
            self.assertEqual(b,  oldEventSort(a))
