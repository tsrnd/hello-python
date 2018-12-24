def merge(array):
    l, m, h = 0, len(array) // 2, len(array)
    l1, l2, i = l, m, l
    res = [0]*h
    while l1 < m and l2 < h:
        if array[l1] <= array[l2]:
            res[i] = array[l1]
            l1 += 1
        else:
            res[i] = array[l2]
            l2 += 1
        i += 1
    while l1 < m:
        res[i] = array[l1]
        i += 1
        l1 += 1

    while l2 < h:
        res[i] = array[l2]
        i += 1
        l2 += 1

    for i in range(l, h):
        array[i] = res[i]
    return res

def selectionSort(arr):
    for i in range(len(arr)):  
        minIndex = i    
        for j in range(i+1, len(arr)): 
            if arr[minIndex] > arr[j]: 
                minIndex = j 
                arr[i], arr[minIndex] = arr[minIndex], arr[i] 
    return arr

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
            self.assertEqual(selectionSort(cases), sorted(cases))
            self.assertEqual(merge(cases), sorted(cases))

if __name__ == '__main__':
    unittest.main()
    
