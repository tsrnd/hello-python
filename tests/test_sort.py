import random
from main import quickSort, shellSort

const_round = 100
const_min_random = -100000
const_max_random = 100000
const_limit_case = 10000

#test quicksort with 100 list(10000)
def testQuickSort():
    for _ in range(const_round):
        case = [random.randint(const_min_random, const_max_random) for _ in range(const_limit_case)]
        case_copy = case.copy()
        case_copy.sort()
        assert case_copy, quickSort(case)

#test shellsort with 100 list(10000)
def testShellSort():
    for _ in range(const_round):
        case = [random.randint(const_min_random, const_max_random) for _ in range(const_limit_case)]
        case_copy = case.copy()
        case_copy.sort()
        assert case_copy, shellSort(case)
