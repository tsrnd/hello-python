import unittest, d4func as f
    
class TestDemo(unittest.TestCase):
    def test_1(self):
        self.assertTrue(f.checkPrime(7))

    def test_2(self):
        self.assertTrue(f.makeThisNotCoverage(1))
        # self.assertFalse(f.makeThisNotCoverage(0))

a = TestDemo()
if __name__ == '__main__':
    unittest.main()