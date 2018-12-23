import random, pytest, unittest
from sort_algo import quickSort, insertSort
def randomList(n, begin, end):
    l = []
    for _ in range(n):
        l.append(random.randint(begin, end+1))
    return l

class MyTest(unittest.TestCase):
    def testSort(self):
        for _ in range(100):
            list = randomList(10000, -10000, 10000)
            sorted_list = sorted(list)
            assert insertSort(list)== sorted_list
            assert quickSort(list) == sorted_list
