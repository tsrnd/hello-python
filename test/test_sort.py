import unittest, random, pytest
from main import heapSort, quickSort, selectionSort
  
def Rand(start, end, num): 
    res = [] 
    for _ in range(num): 
        res.append(random.randint(start, end)) 
    return res 

 
  
class testQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        for _ in range(100):
            array = Rand(-100000, 100000, 10000)
            arraysort = array.copy()
            arraysort.sort()
            self.assertEqual(quickSort(array,0,10000-1), arraysort)
 
  
class TestHeapSort(unittest.TestCase):
    def test_heap_sort(self):
        for _ in range(100):
            array = Rand(-100000, 100000, 10000)
            arraysort = array[:]
            arraysort.sort()
            self.assertEqual(heapSort(array), arraysort)

