import unittest
import module_factorial as fac
import module_fibonacci as fibo


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        test_cases = [
            {"input": 3, "output": 6},
            {"input": 1, "output": 1},
            {"input": 4, "output": 24},
            {"input": 9, "output": 362880},
        ]
        for test_case in test_cases:
            self.assertEqual(fac.factorial(test_case["input"]), test_case["output"])


class TestFibonacci(unittest.TestCase):
    def test_fibo(self):
        self.assertEqual(fibo.fibo(2), 1)

    def test_fibo2(self):
        self.assertEqual(fibo.fibo2(8), 6)


unittest.main()

