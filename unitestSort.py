import unittest, random
from quicksort import quickSort
from selectionsort import selectionSort
  
def randomList(n, begin, end):
    l = []
    for _ in range(n):
        l.append(random.randint(begin, end + 1))
    return l
 
  
class testQuickSort(unittest.TestCase):
    def test_merge_sort(self):
        for _ in range(100):
            array = randomList(10000, -100000, 10000)
            arraysort = array.copy()
            arraysort.sort()
            self.assertEqual(quickSort(array,0,10000-1), arraysort)
 
  
class TestCountingSort(unittest.TestCase):
    def test_counting_sort(self):
        for _ in range(100):
            array = randomList(10000, -100000, 100001)
            arraysort = array[:]
            arraysort.sort()
            self.assertEqual(selectionSort(array,10000), arraysort)