import unittest
import exam_functions as exMod


class TestForFunction(unittest.TestCase):

    def test_recursionFactorial_min(self):
        """Method test normal."""
        self.assertEqual(exMod.recursionFactorial(1), 1)

    def test_recursionFactorial_zero(self):
        """Method test for calculate Factorial 0."""
        with self.assertRaises(Exception) as context:
            exMod.recursionFactorial(0)
        self.assertTrue(
            'Can not calculate factorial for 0.' in str(context.exception))

    def test_recursionFactorial_notDigit(self):
        """Method test for calculate Factorial of character."""
        with self.assertRaises(Exception) as context:
            exMod.recursionFactorial('a')
        self.assertTrue('It is not digit.' in str(context.exception))

    def test_quadratic_function_AisNotDigit(self):
        """Method test check A parameter is not digit."""
        with self.assertRaises(Exception) as context:
            exMod.quadratic_function('a', 2, 4)
        self.assertTrue('input number doesn\'t number. ' in str(context.exception))

    def test_quadratic_function_BisNotDigit(self):
        """Method test check B parameter is not digit."""
        with self.assertRaises(Exception) as context:
            exMod.quadratic_function(1, 'b', 4)
        self.assertTrue('input number doesn\'t number. ' in str(context.exception))

    def test_quadratic_function_CisNotDigit(self):
        """Method test check C parameter is not digit."""
        with self.assertRaises(Exception) as context:
            exMod.quadratic_function(1, 2, 'c')
        self.assertTrue('input number doesn\'t number. ' in str(context.exception))

    def test_quadratic_function(self):
        """Method test for method quadratic."""
        lambFunc = exMod.quadratic_function(1, 2, 5)
        result = lambFunc(5)
        self.assertEqual(result, 40)

    def test_quadratic_function_Negative(self):
        """Method test for method quadratic with some negative value."""
        lambFunc = exMod.quadratic_function(7, -6, -2)
        result = lambFunc(5)
        self.assertEqual(result, 143)

if __name__ == "__main__":
    unittest.main()
