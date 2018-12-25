import random, pytest, unittest
from quick_sort import quicksort
from insertion_sort import insertionSort

def randomList(number, min, max):
    l = []
    for _ in range(number):
        l.append(random.randint(min, max+1))
    return l

class MyTest(unittest.TestCase):
    def testSort(self):
        for _ in range(100):
            list = randomList(100, -10000, 10000)
            sorted_list = sorted(list)
            assert insertionSort(list)== sorted_list
            assert quicksort(list) == sorted_list