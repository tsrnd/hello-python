import unittest
def cocktailShakerSort(array):
    start = 0
    end = len(array)
    while start != end:
        for i in range(start, end - 1):
            if array[i] > array[i + 1]:
                tam = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tam
        end -= 1
        if end == start:
            return array
        for i in range(0, end - start):
            j = end - i
            if array[j] < array[j - 1]:
                tam = array[j]
                array[j] = array[j - 1]
                array[j - 1] = tam
        start += 1
    return array

class TestSort(unittest.TestCase):
    testcase = [[1,3,4,4,7,23,53,75,34,2,54,3,3,6,245],
            [5,3,4,6,3,6,8,43,653,436,666,777,33,224,65],
            [454,34,12,64,7,33],
            [3]]
    result =   [[1, 2, 3, 3, 3, 4, 4, 6, 7, 23, 34, 53, 54, 75, 245],
                [3, 3, 4, 5, 6, 6, 8, 33, 43, 65, 224, 436, 653, 666, 777],
                [7, 12, 33, 34, 64, 454],
                [3]]
    def test(self):
        for i in range(0, len(self.testcase)):
            self.assertEqual(cocktailShakerSort(self.testcase[i]), self.result[i])
if __name__ == '__main__':
    unittest.main()