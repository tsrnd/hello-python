import unittest
from Day03 import display
class DisplayTest(unittest.TestCase) :
    def test_display_method(self):
        self.assertEqual(display.display_method(), 'this is display method')
