import unittest, random, pytest
from main import quickSort, selectionSort
  
def Rand(start, end, num): 
    res = [] 
    for j in range(num): 
        res.append(random.randint(start, end)) 
    return res 

 
  
class testQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        for _ in range(100):
            array = Rand(-100000, 100000, 100)
            arraysort = array.copy()
            arraysort.sort()
            self.assertEqual(quickSort(array,0,100-1), arraysort)
 
  
class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        for _ in range(100):
            array = Rand(-100000, 100000, 100)
            arraysort = array[:]
            arraysort.sort()
            self.assertEqual(selectionSort(array,100), arraysort)