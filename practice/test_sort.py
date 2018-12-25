import random
import unittest


def mergeSort(arr):
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid] 
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1

        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1

        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

    return arr


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


class TestSorting(unittest.TestCase):
    maxDiff = None
    min_range = -100000
    max_range = 100000
    count = 10000
    number_of_cases = 100

    def testSort(self):
        for _ in range(self.number_of_cases):
            cases = [random.uniform(self.min_range, self.max_range)
                     for _ in range(self.count)]
            # assert quickSort(cases) == sorted(cases)
            assert mergeSort(cases) == sorted(cases)
