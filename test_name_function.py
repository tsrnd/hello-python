import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Vo Van Nghia?"""
        formatted_name = get_formatted_name('vo van', 'nghia')
        self.assertEqual(formatted_name, 'Vo Van Nghia')
