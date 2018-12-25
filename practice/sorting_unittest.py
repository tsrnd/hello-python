def countingSort(array):
    maxArray, minArray = max(array), min(array)
    res = []
    listIndex = [0] * (maxArray - minArray + 1)
    for i in array:
        listIndex[i + abs(minArray) - 1] += 1
    for i in range(minArray, maxArray + 1):
        while listIndex[i + abs(minArray) - 1]:
            listIndex[i + abs(minArray) - 1] -= 1
            res.append(i)
    return res

def quickSort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quickSort(less)+equal+quickSort(greater)
    else:
        return array

import unittest, random

class TestSorting(unittest.TestCase):
    maxDiff = None
    min_range = -100000
    max_range = 100000
    count = 10000
    number_of_cases = 100

    def testSort(self):
        for _ in range(self.number_of_cases):
            cases = [random.randrange(self.min_range, self.max_range) for _ in range(self.count)]
            # assert quickSort(cases) == sorted(cases)
            assert countingSort(cases) == sorted(cases)

