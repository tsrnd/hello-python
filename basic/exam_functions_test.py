import unittest
import exam_functions as exMod

class TestForFunction(unittest.TestCase):

    def test_recursionFactorial_min(self):
        """
            Method test normal.
        """
        self.assertEqual(exMod.recursionFactorial(1), 1)

    def test_recursionFactorial_zero(self):
        """
            Method test for calculate Factorial 0.
        """
        with self.assertRaises(Exception) as context:
            exMod.recursionFactorial(0)
        self.assertTrue('Can not calculate factorial for 0.' in str(context.exception))
    

if __name__ == "__main__":
    unittest.main()