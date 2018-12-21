import unittest
import d3_common


def add(x, y):
    return x + y


# TestD3Common unit test
class TestD3Common(unittest.TestCase):
    def test_factorial(self):
        test_cases = [
            {"input": 2, "output": 2},
            {"input": 3, "output": 6},
            {"input": 4, "output": 24},
        ]
        for test_case in test_cases:
            self.assertEqual(
                d3_common.factorial(test_case["input"]), test_case["output"]
            )

    def test_devide(self):
        self.assertEqual(d3_common.devide(2, 1), 2)
        with self.assertRaises(ValueError):
            d3_common.devide(2, 0)


if __name__ == "__main__":
    unittest.main()
