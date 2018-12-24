import unittest
import random
import bucket_sort

def random_array(min_value, max_value, element_number):
    case_test = [random.randint(min_value, max_value)
        for _ in range(element_number)]
    return case_test


def test_bucket_sort():
    case_test = random_array(-100000, 100000, 10000)
    for _ in range(100):
        case_test = random_array(-100000, 100000, 10000)
        assert sorted(case_test) == bucket_sort.sort(case_test, 1000)
