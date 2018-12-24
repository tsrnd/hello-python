import random
from main import bubbleSort, insertionSort

const_round = 100
const_min_random = -100000
const_max_random = 100000
const_limit_case = 100

#test bubblesort with 100 list(10000)
def testBubbleSort():
    for _ in range(const_round):
        case = [random.randint(const_min_random, const_max_random) for _ in range(const_limit_case)]
        case_copy = case.copy()
        case_copy.sort()
        assert case_copy, bubbleSort(case)

#test insertion  with 100 list(10000)
def testInsertionSort():
    for _ in range(const_round):
        case = [random.randint(const_min_random, const_max_random) for _ in range(const_limit_case)]
        case_copy = case.copy()
        case_copy.sort()
        assert case_copy, insertionSort(case)
