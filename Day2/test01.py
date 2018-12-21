import unittest

def factorial(n):
    if n == 0: return 1
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

print(factorial(8))

class TestFactorialMethod(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0),1)

if __name__ == '__main__':
    unittest.main()