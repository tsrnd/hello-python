import pytest
import unittest
from main import polymorphism


class UnitTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(10, polymorphism.add(2, 3, 5))
