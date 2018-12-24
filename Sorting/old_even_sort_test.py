import unittest
import old_even_sort
import random


class OldEventSortTest(unittest.TestCase):
    def test_old_event_sort(self):
        list = [random.uniform(-100000,100000) for _ in range(10000)]
        old_even_sort.old_even_sort(list)
        self.assertGreaterEqual(list[3], list[1])
