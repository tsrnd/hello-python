import unittest
from unittest import mock

class Demo:
    def test(self, n):
        if n == 1:
            return "1"
        if n == 2:
            return "2"

class TestSomthing(unittest.TestCase):
    def mock_search(self):
        class MockDemo(Demo):
            def __iter__(self):
                return iter("2")
        return MockDemo()

    @mock.patch('__main__.Demo', mock_search)
    def test_demo(self):
        self.assertEqual(3, 4)

test = TestSomthing()

test.test_demo()
