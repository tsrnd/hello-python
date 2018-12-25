import unittest
from bubble_sort_func import buddle_sort
from insertion_sort import get_insertion_sort

array = [1, 3, 2, 5, 7, 5, 6, 8]


class NameTestCase(unittest.TestCase):
    """Test buddle sort."""

    def test_buddle_sort(self):
        x = buddle_sort(array)
        y = get_insertion_sort(array)
        self.assertEqual(x, [1, 2, 3, 5, 5, 6, 7, 8])
        self.assertEqual(y, [1, 2, 3, 5, 5, 6, 7, 8])
