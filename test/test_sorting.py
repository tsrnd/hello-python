from sorting import *
import random
import pytest


def random_input_array():
    array = []
    for _ in range(9999):
        array.append(random.randint(-100000, 100000))
    return array


def create_input_test():
    result = []
    for _ in range(50):
        a = random_input_array()
        result.append(a)
    return result


@pytest.fixture(params=create_input_test())
def data(request):
    return request.param


def test_quick_sort(data):
    b = sorted(data)
    assert b == quickSort(data)


def test_heap_sort(data):
    b = sorted(data)
    assert b == heapSort(data)
